from django.contrib import admin
from .models import Warehouse, MaterialMaster, MaterialType


admin.site.register(Warehouse)
admin.site.register(MaterialMaster)
admin.site.register(MaterialType)