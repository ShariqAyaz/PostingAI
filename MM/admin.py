from asyncio import format_helpers
from audioop import reverse
from urllib.parse import urlencode
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GrnItemsDet, PaymentMethods, Warehouse, MaterialMaster, MaterialType,GrnNote


class GrnNoteInline(admin.TabularInline):
    model = GrnItemsDet

class GrnDetAdmin(admin.ModelAdmin):
    inlines = [
        GrnNoteInline
    ]

    list_display = ('invoiceNumber', 'vendorName', 'date', 'isPosted')

    @receiver(post_save, sender=GrnItemsDet)
    def my_handler(sender, **kwargs):
        print(sender.objects.all())


    

admin.site.register(PaymentMethods)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnDetAdmin)
admin.site.register(GrnItemsDet)