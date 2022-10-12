from decimal import Decimal
import numbers
from unicodedata import decimal
from django.dispatch import Signal, receiver
from django.contrib import admin
from django.db.models.signals import post_save, pre_delete, pre_save 
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta
from POS.models import Menuitems, Recipeitems, Recipes, Inventoryitems, Inventorytransactiondocuments, Inventorytransactions, Menuitemportions, Menuitemprices
from .models import GrnItemsDet, PaymentMethods, Warehouse, InternalMaterial, MaterialMaster, MaterialType, GrnNote, Store, StoreDet, Products, Recipe, RecipeItems, ProcessedProduct, SaleProduction, SaleProcessedProduct, WastageProduct, WastageRawMaterial


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'SambaPOS3'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class GrnNoteInline(admin.TabularInline):
    model = GrnItemsDet


class GrnDetAdmin(admin.ModelAdmin):
    list_display = (
        'grn_no', 'itemName', 'irate', 'iqty', 'Amount'
    )

    def Amount(self, obj):
         return 'obj.Amount'

class GrnNoteAdmin(admin.ModelAdmin):
    inlines = [
        GrnNoteInline
    ]
    list_display = ('invoiceNumber', 'vendorName', 'date', 'isPosted')

    @receiver(post_save)
    def post_handler(sender, created=False, deleted=False, instance=None, *args, **kwargs):
        
        lst_models = ('GrnNote', 'GrnItemsDet', 'Store', 'StoreDet')

        if sender.__name__ in lst_models:
            cur_grn_no = None

            if sender.__name__ == 'GrnNote':
                current_grn_obj = (sender.objects.get(id=instance.id))
                cur_grn_no = instance.id
                if created:
                    if current_grn_obj.isPosted == True:
                        store = Store.objects.create(ref_doc_no=cur_grn_no, docType='GRN', doc_date=current_grn_obj.date)
                        store.save()
                    else:
                        pass

            if sender.__name__ == 'GrnItemsDet':
                obj = sender.objects.select_related('itemName').values(
                    'itemName__UOP',
                    'itemName__internalName',
                    'itemName__packingOf',
                    'itemName__unitSize',
                    'itemName__UOC'
                    ).filter(itemName=instance.itemName).first()

                imObj = MaterialMaster.objects.filter(internalName=obj.get('itemName__internalName')).first()
                    
                packing_of = obj.get('itemName__packingOf')
                unitSize = obj.get('itemName__unitSize')
                qty_each = packing_of * unitSize

                if created:
                    store_doc_id = Store.objects.filter(ref_doc_no=str(instance.grn_no), docType='GRN').first()
                    StoreDet.objects.create(doc=store_doc_id, itemName=imObj.internalName, increase_qty=instance.iqty*qty_each, decrease_qty=0)
                else:
                    store_doc_id = Store.objects.filter(ref_doc_no=str(instance.grn_no), docType='GRN').first()                    
                    StoreDet.objects.filter(doc=store_doc_id, itemName=imObj.internalName).update(increase_qty=instance.iqty*qty_each, decrease_qty=0)

    @receiver(pre_delete)
    def post_handler(sender, instance=None, *args, **kwargs):
        
        lst_models = ('GrnNote', 'GrnItemsDet', 'Store', 'StoreDet')
        if sender.__name__ in lst_models:
            if sender.__name__ == 'GrnItemsDet':
                store_doc_id = Store.objects.filter(ref_doc_no=str(instance.grn_no), docType='GRN').first()                    
                StoreDet.objects.filter(doc=store_doc_id, itemName=instance.itemName).delete()

class StoreDetAdmin(admin.ModelAdmin):
    list_display = (
        'doc','itemName','increase_qty','decrease_qty'
        )


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'ref_doc_no', 'docType', 'doc_date'
        )
        
class MaterialMasterAdmin(admin.ModelAdmin):
    list_display = (
        'internalName', 'name', 'UOP', 'UOC', 'packingOf', 'unitSize'
    )

admin.site.register(PaymentMethods)
admin.site.register(InternalMaterial)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster, MaterialMasterAdmin)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnNoteAdmin)
admin.site.register(GrnItemsDet, GrnDetAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreDet, StoreDetAdmin)
admin.site.register(Products)
admin.site.register(Recipe)
admin.site.register(RecipeItems)
admin.site.register(ProcessedProduct)
admin.site.register(SaleProduction)
admin.site.register(SaleProcessedProduct)
admin.site.register(WastageProduct)
admin.site.register(WastageRawMaterial)