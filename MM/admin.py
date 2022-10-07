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
    def my_handler(sender, created, instance, **kwargs):

        current_grn = (sender.objects.get(id=instance.id))

        if instance.id != None:
            print('Instance id: ' + str(instance.id))

            if created:
                if current_grn.isPosted == True:
                    print('NEW\nPosted Marked ' + str(True))
                else:
                    print('NEW\nNot Posted Marked ' + str(False))

            else:
                print(current_grn.isPosted)
                
                if current_grn.isPosted == True:
                    print('UPDATED\nPosted Marked ' + str(True))
                else:
                    print('UPDATED\nNot Posted Marked ' + str(False))



admin.site.register(PaymentMethods)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnDetAdmin)
admin.site.register(GrnItemsDet)