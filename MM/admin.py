from django.contrib import admin
from .models import GrnItemsDet, PaymentMethods, Warehouse, MaterialMaster, MaterialType,GrnNote


class GrnNoteInline(admin.TabularInline):
    model = GrnItemsDet

class GrnDetAdmin(admin.ModelAdmin):
    inlines = [
        GrnNoteInline
    ]

    def invoiceNumber(self,obj):
        return obj.get_value()

admin.site.register(PaymentMethods)
admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)
admin.site.register(GrnNote,GrnDetAdmin)
admin.site.register(GrnItemsDet)