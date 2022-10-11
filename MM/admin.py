from decimal import Decimal
import numbers
from unicodedata import decimal
from django.dispatch import Signal, receiver
from django.contrib import admin
from django.db.models.signals import post_save, pre_delete, pre_save 
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta
from .models import GrnItemsDet, PaymentMethods, Warehouse, InternalMaterial, MaterialMaster, MaterialType, GrnNote, Store, StoreDet


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
                obj = sender.objects.select_related('itemName').values('itemName__UOP','itemName__internalName','itemName__packingOf','itemName__unitSize','itemName__UOC').filter(itemName=instance.itemName).first()
                packing_of = obj.get('itemName__packingOf')
                unitSize = obj.get('itemName__unitSize')
                qty_each = packing_of * unitSize
                if created:
                    store_doc_id = Store.objects.filter(ref_doc_no=str(instance.grn_no), docType='GRN').first()    
                    StoreDet.objects.create(doc=store_doc_id, itemName=instance.itemName, increase_qty=instance.iqty*qty_each, decrease_qty=0)
                else:
                    store_doc_id = Store.objects.filter(ref_doc_no=str(instance.grn_no), docType='GRN').first()                    
                    StoreDet.objects.filter(doc=store_doc_id, itemName=instance.itemName).update(increase_qty=instance.iqty*qty_each, decrease_qty=0)

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