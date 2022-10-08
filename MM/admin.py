from asyncio import format_helpers
from audioop import reverse
from urllib.parse import urlencode
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta
from .models import GrnItemsDet, PaymentMethods, Warehouse, MaterialMaster, MaterialType, GrnNote, Store, StoreDet


class GrnNoteInline(admin.TabularInline):
    model = GrnItemsDet

# https://stackoverflow.com/questions/8541956/django-admin-add-extra-row-with-totals
class GrnDetAdmin(admin.ModelAdmin):
    list_display = (
        'grn_no', 'itemName', 'irate', 'iqty', 'Amount'
    )

    def Amount(self, obj):
         return 'obj.Amount'

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.annotate(
    #         #_lineitem_amt=sum('irate'*'iqty')
    #     )
    #     return queryset


class GrnNoteAdmin(admin.ModelAdmin):
    inlines = [
        GrnNoteInline
    ]

    list_display = ('invoiceNumber', 'vendorName', 'date', 'isPosted')

    @receiver(post_save, sender=GrnNote)
    def my_handler(sender, created, instance, **kwargs):

        current_grn = (sender.objects.get(id=instance.id))

        if instance.id != None:
            print('Instance id: ' + str(instance.id))

            if created:
                if current_grn.isPosted == True:
                    
                    Store.objects.create(ref_doc_no=current_grn.id,docType='GRN',doc_date=current_grn.date)

                    print('NEW\nPosted Marked ' + str(True))
                else:
                    print('NEW\nNot Posted Marked ' + str(False))

            else:

                if current_grn.isPosted == True:
                    print('UPDATED\nPosted Marked ' + str(True))
                    
                    # Posting after unposting old data: 'Store' , 'StoreDet'
                    if Store.objects.filter(ref_doc_no=current_grn.id,docType='GRN').count() > 0:
                        print('Found in Store? matched with instance and doctype GRN')
                    # Posting first time: 'Store' , 'StoreDet'
                    else:

                        print('\t\nNot in Store? not matched with instance id and doctype GRN\n')
                        print('Storing...\n')
                        # Storing for the first time
                        Store.objects.create(ref_doc_no=current_grn.id,docType='GRN',doc_date=current_grn.date)
                        print('Stored\n')

                else:

                    if Store.objects.filter(ref_doc_no=current_grn.id,docType='GRN').count() > 0:
                        print('unposting from Store and StoreDet...')

                    print('UPDATED\nNot Posted Marked ' + str(False))


admin.site.register(PaymentMethods)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnNoteAdmin)
admin.site.register(GrnItemsDet, GrnDetAdmin)