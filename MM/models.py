from email.policy import default
from sqlite3 import Timestamp
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

###############
# Warehouse < #
###############
WAREHOUSE_TYPES = (
    ('Frozen','Frozen'),
    ('Cold','Cold'),
    ('Dry','Dry'),
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

class MaterialMaster(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False,blank=False,verbose_name='Material Name')
    internalName = models.CharField(max_length=255, unique=False, null=False,blank=False,verbose_name='Material Internal Name', help_text='i.e (milk, egg, chicken, tuna) in respective unit')
    barcode = models.CharField(max_length=255,unique=True,blank=True,null=True, verbose_name='Barcode')
    warehouse = models.ForeignKey('Warehouse',models.DO_NOTHING, verbose_name='Where it Store / Warehouse',help_text='Where it is store, internaly after inward')
    type = models.ForeignKey('MaterialType', models.DO_NOTHING,null=False,verbose_name='Material Type',help_text='for example: Storing Tuna type is Meat, Seafood, and Poultry')
    UOP = models.CharField(max_length=25, choices=MEASURE_UNITS, unique=False, null=False, verbose_name='Unit of Measure Purchase')
    UOC = models.CharField(max_length=25, choices=MEASURE_UNITS, unique=False, null=False, verbose_name='Unit of Measure Consume', help_text='note: Unit of consume will be the unit used to store stock and to move inventory')
    packingOf = models.DecimalField(max_digits=18, decimal_places=4, help_text='For example: Convert from Purchase to Consume unit.In which Unit of Measure material will consume. Further, if bough box of 24pcs, so 24 will be assign here, if consume in box. if each box having item in Kgs, then 24xWeight of each Pcs within carton')
    unitSize = models.DecimalField(max_digits=18, decimal_places=4,help_text='Important: If Purchase unit and sale units are not same, than provide unit of consumtion quantity/weights')
    
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
class GrnNote(models.Model):
    invoiceNumber = models.CharField(max_length=50, verbose_name='Supplier / Vendor Invoice number')
    paymentMethod = models.ForeignKey('PaymentMethods', models.DO_NOTHING)
    vendorName = models.CharField(max_length=60, verbose_name='Supplier/Vendor Name')
    date = models.DateTimeField(verbose_name="Date of Invoice")
    isPosted = models.BooleanField(default=False)
    note = models.CharField(max_length=100, blank=True, null=False, default='N/A')
    time_stamp = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    
    def __init__(self, *args, **kwargs):
        super(GrnNote, self).__init__(*args, **kwargs)
        self.__origin = self.id

    def __str__(self):
        return f"{self.pk}" 

class GrnItemsDet(models.Model):
    grn_no = models.ForeignKey('GrnNote', models.DO_NOTHING)
    itemName = models.ForeignKey('MaterialMaster', models.DO_NOTHING)
    irate = models.DecimalField(max_digits=18, decimal_places=4)
    iqty = models.DecimalField(max_digits=18, decimal_places=4)

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
    ('Transfer','Transfer'), # Apply When Raw Material Issue to Production unit for process, Decrease Stock
    ('Wastage','Wastage'),  # Apply When Raw Material got expire to be discard, Decrease Stock
)
class Store(models.Model):
    ref_doc_no = models.IntegerField()
    docType = models.CharField(max_length=15, choices=REF_DOC_TYPE, unique=False, null=False)
    doc_date = models.DateTimeField()

    def __str__(self):
        return f"{self.ref_doc_no}"
    
    class Meta:
        unique_together = (('ref_doc_no', 'docType'),)


class StoreDet(models.Model):
    doc = models.ForeignKey(Store, models.DO_NOTHING)
    itemName = models.ForeignKey('MaterialMaster', models.DO_NOTHING)
    increase_qty = models.DecimalField(max_digits=18, decimal_places=4)
    decrease_qty = models.DecimalField(max_digits=18, decimal_places=4)

    def __str__(self):
        return f"{self.id}"

###########################
# Store Stock Warehouse > #
###########################