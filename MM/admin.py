from asyncio import format_helpers
from audioop import reverse
from urllib.parse import urlencode
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GrnItemsDet, PaymentMethods, Warehouse, MaterialMaster, MaterialType, GrnNote


class GrnNoteInline(admin.TabularInline):
    model = GrnItemsDet

class GrnDetAdmin(admin.ModelAdmin):
    inlines = [
        GrnNoteInline
    ]

    list_display = ('invoiceNumber', 'vendorName', 'date', 'isPosted')

    @receiver(post_save, sender=GrnNote)
    def my_handler(sender, created, **kwargs):

        if created:
            last_grn = (sender.objects.last())
            pm = PaymentMethods.objects.get(name=last_grn.paymentMethod)

            # IF isPosted True checked at the Update event
            if True:
                print(True)
            # IF isPosted False checked at the Update event
            else:
                print(False)

            print(pm.id)
            print(last_grn)
            
            # for k in last_grn:
            #     pm = PaymentMethods.objects.filter(name=k.paymentMethod)
            #     print(pm)
        else:
            print('UPDATED?\n')

            # IF isPosted True checked at the Update event
            if True:
                print(True)
            # IF isPosted False checked at the Update event
            else:
                print(False)

    # @receiver(post_save, sender=GrnItemsDet)
    # def my_handler(sender, **kwargs):
    #     last_grn = (sender.objects.last())
    #     #pm = PaymentMethods.objects.get(name=last_grn.paymentMethod)
    #     #print(pm.id)
    #     print(last_grn)
    #     # for k in last_grn:
    #     #     pm = PaymentMethods.objects.filter(name=k.paymentMethod)
    #     #     print(pm)

admin.site.register(PaymentMethods)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnDetAdmin)
admin.site.register(GrnItemsDet)