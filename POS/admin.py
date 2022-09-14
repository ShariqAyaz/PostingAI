import imp
from socket import fromshare
from django.contrib import admin
from django.db import models
from .models import Menuitems, Recipeitems, Recipes, Inventoryitems, Inventorytransactiondocuments, Inventorytransactions, Menuitemportions, Menuitemprices
from django import forms



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


class RecipeitemsAdminTab(admin.TabularInline):
    using = 'SambaPOS3'
    def get_queryset(self, request):
        # Tell Django to look for inline objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class RecipeitemsAdmin(RecipeitemsAdminTab):
    model = Recipeitems


class RecipesAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'SambaPOS3'
    inlines = [RecipeitemsAdmin,]

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




admin.site.register(Menuitems,MultiDBModelAdmin)
admin.site.register(Recipeitems,MultiDBModelAdmin)
admin.site.register(Recipes,RecipesAdmin)
admin.site.register(Inventoryitems,MultiDBModelAdmin)
admin.site.register(Inventorytransactiondocuments,MultiDBModelAdmin)
admin.site.register(Inventorytransactions,MultiDBModelAdmin)
admin.site.register(Menuitemportions,MultiDBModelAdmin)
admin.site.register(Menuitemprices,MultiDBModelAdmin)