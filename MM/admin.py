from django.dispatch import Signal, receiver
from django.contrib import admin
from django.db.models.signals import post_save, pre_delete, pre_save 
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta
from .models import GrnItemsDet, PaymentMethods, Warehouse, MaterialMaster, MaterialType, GrnNote, Store, StoreDet


class GrnNoteInline(admin.TabularInline):
    model = GrnItemsDet


class GrnDetAdmin(admin.ModelAdmin):
    list_display = (
        'grn_no', 'itemName', 'irate', 'iqty', 'Amount'
    )

    @receiver(post_save)
    def post_handler(sender, created=False, instance=None, *args, **kwargs):
        store_doc_no = None
        cur_grn_no = None

        if sender.__name__ == 'GrnItemsDet':

            cur_grn_no = instance.grn_no
            xx = str(cur_grn_no)
            print(cur_grn_no)
            print(xx)
            store_doc_no = Store.objects.filter(ref_doc_no=xx).first()
            StoreDet.objects.create(doc=store_doc_no, itemName=instance.itemName, increase_qty=instance.iqty, decrease_qty=0)
            

    def Amount(self, obj):
         return 'obj.Amount'


class GrnNoteAdmin(admin.ModelAdmin):
    inlines = [
        GrnNoteInline
    ]

    list_display = ('invoiceNumber', 'vendorName', 'date', 'isPosted')

    @receiver(post_save)
    def post_handler(sender, created=False, instance=None, *args, **kwargs):
        
        lst_models = ('GrnNote', 'GrnItemsDet', 'Store', 'StoreDet')

        if sender.__name__ in lst_models:
            cur_grn_no = None

            if sender.__name__ == 'GrnNote':
                current_grn_obj = (sender.objects.get(id=instance.id))
                cur_grn_no = current_grn_obj.id
                if created:
                    if current_grn_obj.isPosted == True:
                        store = Store.objects.create(ref_doc_no=cur_grn_no, docType='GRN', doc_date=current_grn_obj.date)
                        store.save()
                    else:
                        print('GrnNote: On Update Event')


class StoreDetAdmin(admin.ModelAdmin):
    list_display = (
        'doc','itemName','increase_qty','decrease_qty'
        )
        

admin.site.register(PaymentMethods)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnNoteAdmin)
admin.site.register(GrnItemsDet, GrnDetAdmin)
admin.site.register(Store)
admin.site.register(StoreDet, StoreDetAdmin)