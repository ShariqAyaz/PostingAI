######################################################################################
# Author: Muhammad Shariq Ayaz
# Date: 2022
# Description: Costing for RAW material towards finisehd goods and costing
#
# Multiple Databases integration with DJANGO APP
######################################################################################

from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


###############
# Warehouse < #
###############
WAREHOUSE_TYPES = (
    ('Frozen','Frozen'),
    ('Cold','Cold'),
    ('Dry','Dry'),
    ('General','General'),
    ('Misc.','Misc.')
)

class Warehouse(models.Model):
    name = models.CharField(max_length=20,blank=False, null=False, unique=True, verbose_name='Warehouse Name')
    whtype = models.CharField(max_length=25, choices=WAREHOUSE_TYPES, blank=False, null=False, verbose_name='Warehouse Type', help_text='describe, is it consider COLD, Misc, Frozen...')
    location = models.CharField(max_length=50, blank=True, null=False, default='N/A', verbose_name='Location', help_text='describe where it is stack.')

    def __str__(self):
        return self.name
###############
# Warehouse > #
###############

###############
# Material < #
###############
MEASURE_UNITS = (
    ('Kilogram','Kilogram'),
    ('Gram','Gram'),
    ('Milligram','Milligram'),
    ('Litre','Litre'),
    ('Pint','Pint'),
    ('Millilitre','Millilitre'),
    ('Tablespoon','Tablespoon'),
    ('Teaspoon','Teaspoon'),
    ('Box','Box'),
    ('Carton','Carton'),
    ('Pc','Pc'),
    ('Dozen','Dozen'),
    ('Bottle','Bottle'),
)

class InternalMaterial(models.Model):
    internalName = models.CharField(max_length=255, unique=True, null=False,blank=False,verbose_name='Internal Material Name')

    def __str__(self):
        return self.internalName


class MaterialMaster(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False,blank=False,verbose_name='Material Name')
    internalName = models.ForeignKey('InternalMaterial',models.DO_NOTHING,verbose_name='Material Internal Name', help_text='i.e (milk, egg, chicken, tuna) in respective unit')
    barcode = models.CharField(max_length=255,unique=True,blank=True,null=True, verbose_name='Barcode')
    warehouse = models.ForeignKey('Warehouse',models.DO_NOTHING, verbose_name='Where it Store / Warehouse',help_text='Where it is store, internaly after inward')
    type = models.ForeignKey('MaterialType', models.DO_NOTHING,null=False,verbose_name='Material Type',help_text='for example: Storing Tuna type is Meat, Seafood, and Poultry')
    UOP = models.CharField(max_length=25, choices=MEASURE_UNITS, unique=False, null=False, verbose_name='Unit of Measure Purchase')
    UOC = models.CharField(max_length=25, choices=MEASURE_UNITS, unique=False, null=False, verbose_name='Unit of Measure Consume', help_text='note: Unit of consume will be the unit used to store stock and to move inventory')
    packingOf = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4, help_text='For example: Convert from Purchase to Consume unit.In which Unit of Measure material will consume. Further, if bough box of 24pcs, so 24 will be assign here, if consume in box. if each box having item in Kgs, then 24xWeight of each Pcs within carton')
    unitSize = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4,help_text='Important: If Purchase unit and sale units are not same, than provide unit of consumtion quantity/weights')
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        unique_together = (('name', 'internalName'),('internalName','UOC'))


class MaterialType(models.Model):
    type = models.CharField(unique=True, max_length=50, help_text='for example: Storing Tuna type is Meat, Seafood, and Poultry')

    def __str__(self):
        return f"{self.type}"

    class Meta:
        managed = True
###############
# Material > #
###############

###############
# Payment   < #
###############
class PaymentMethods(models.Model):
    cardEnding = models.CharField(max_length=50, default='Cash', unique=True, verbose_name='Card Number / Cash', help_text='Ending 4 digit of card used or Cash etc...')
    name = models.CharField(max_length=50,default='Cash', unique=True, verbose_name='Owner/Holder Name', help_text='i.e(Shariq Halifax, MPhenom NatWest, Rasa Cash, TripleOne Cash)')

    def __str__(self):
        return self.name
###############
# Payment   > #
###############

#############################
# GRN - Good Receipt Note < #
#############################
class GrnNote(models.Model): # ref_doc_no = GRN
    invoiceNumber = models.CharField(max_length=50, verbose_name='Supplier / Vendor Invoice number')
    paymentMethod = models.ForeignKey('PaymentMethods', models.DO_NOTHING)
    vendorName = models.CharField(max_length=60, verbose_name='Supplier/Vendor Name')
    date = models.DateTimeField(default=now, verbose_name="Date of Invoice")
    isPosted = models.BooleanField(default=True)
    note = models.CharField(max_length=100, blank=True, null=False, default='N/A')
    time_stamp = models.DateTimeField(default=now, verbose_name="Updated at")
    
    def __init__(self, *args, **kwargs):
        super(GrnNote, self).__init__(*args, **kwargs)
        self.__origin = self.id

    def __str__(self):
        return f"{self.pk}" 

class GrnItemsDet(models.Model):
    grn_no = models.ForeignKey('GrnNote', models.DO_NOTHING)
    itemName = models.ForeignKey('MaterialMaster', models.DO_NOTHING)
    irate = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    iqty = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)

    def __str__(self):
        return f"{self.grn_no}"
#############################
# GRN - Good Receipt Note > #
#############################

###########################
# Store Stock Warehouse < #
###########################
REF_DOC_TYPE = (
    ('GRN','GRN'), # Apply when purchase, Increasing Stock
    ('Return','Return'), # Apply when returning to Supplier for any reason, Decrease Stock
    ('PreProduction','PreProduction'), # Apply When Raw Material Issue to Production unit for process, Decrease Stock
    ('Production','Production'), # Apply When Raw Material Issue to Production unit for Sale, Decrease Stock
    ('WastageRaw','WastageRaw'),  # Apply When Raw Material got expire to be discard, Decrease Stock
)
class Store(models.Model):
    ref_doc_no = models.IntegerField()
    docType = models.CharField(max_length=15, choices=REF_DOC_TYPE, unique=False, null=False)
    doc_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.ref_doc_no}"
    
    class Meta:
        unique_together = (('ref_doc_no', 'docType'),)


class StoreDet(models.Model):
    doc = models.ForeignKey(Store, models.DO_NOTHING)
    itemName = models.ForeignKey('InternalMaterial', models.DO_NOTHING)
    increase_qty = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    decrease_qty = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)

    def __str__(self):
        return f"{self.id}"

###########################
# Store Stock Warehouse > #
###########################

##########################
# Production Warehouse < #
##########################
class Products(models.Model):
    ProductNamePos = models.CharField(max_length=150, verbose_name='Product Name', unique=True, null=False)
    ProductIdPos = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='ProductID from POS', help_text='Prodcut ID from POS to map')
    ProductPricePos = models.DecimalField(max_digits=18, verbose_name='Product Price', validators=[MinValueValidator(0.0)], decimal_places=4)

    def __str__(self):
        return f"{self.ProductNamePos}"

class Recipe(models.Model):
    RecipeName = models.CharField(max_length=150, verbose_name='Product Name', unique=True, null=False)
    ProductNamePos = models.ForeignKey('Products', models.DO_NOTHING)
    PreProcess = models.BooleanField(default=False, help_text='If item requires: Produce it first before SOLD, such as biryani then checked it. if it is produce on demand or sold as buy then unchecked it(such as redbull, Panini')

    def __str__(self):
        return f"{self.RecipeName}"

class RecipeItems(models.Model):
    recipeId = models.ForeignKey('Recipe', models.DO_NOTHING)
    itemName = models.ForeignKey('InternalMaterial', models.DO_NOTHING)
    consQty = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)

    def __str__(self):
        return f"{self.recipeId}"

class ProcessedProduct(models.Model): # ref_doc_no = PreProduction
    ProductNamePos = models.ForeignKey('Products', models.DO_NOTHING)
    QuantityProcessed = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    dateofProcessed = models.DateTimeField(default=now,verbose_name="Date of Process")

    def __str__(self):
        return f"{self.ProductNamePos}"

class SaleProduction(models.Model): # ref_doc_no = Production
    ProductNamePos = models.ForeignKey('Products', models.DO_NOTHING)
    QuantitySale = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    dateofSale = models.DateTimeField(default=now,verbose_name="Date of Sale")

    def __str__(self):
        return f"{self.ProductNamePos}"

class SaleProcessedProduct(models.Model): # not hit storedet
    ProductNamePos = models.ForeignKey('Products', models.DO_NOTHING)
    QuantitySale = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    dateofSale = models.DateTimeField(default=now,verbose_name="Date of Sale")

    def __str__(self):
        return f"{self.ProductNamePos}"

class WastageProduct(models.Model): # not hit storedet
    ProductNamePos = models.ForeignKey('Products', models.DO_NOTHING)
    QuantityWastage = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    dateofWastage = models.DateTimeField(default=now,verbose_name="Date of Wastage")

    def __str__(self):
        return f"{self.ProductNamePos}"

class WastageRawMaterial(models.Model): # ref_doc_no = WastageRaw
    itemName = models.ForeignKey('InternalMaterial', models.DO_NOTHING)
    QuantityWastage = models.DecimalField(max_digits=18, validators=[MinValueValidator(0.0)], decimal_places=4)
    dateofWastage = models.DateTimeField(default=now,verbose_name="Date of Wastage")

    def __str__(self):
        return f"{self.itemName}"

##########################
# Production Warehouse > #
##########################
