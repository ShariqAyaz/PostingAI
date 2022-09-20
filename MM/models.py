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
    ('Liter','Liter'),
    ('Pint','Pint'),
    ('Millilitre','Millilitre'),
    ('Tablespoon','Tablespoon'),
    ('Teaspoon','Teaspoon'),
    ('Box','Box'),
    ('Carton','Carton'),
    ('Pcs','Pcs'),
    ('Dozen','Dozen'),
    ('Bottle','Bottle'),
)

class MaterialMaster(models.Model):
    name = models.CharField(max_length=255, unique=False, null=False,blank=False,verbose_name='Material Name')
    internalName = models.CharField(max_length=255, unique=False, null=False,blank=False,verbose_name='Material Internal Name', help_text='i.e (milk, egg, chicken, tuna) in respective unit')
    barcode = models.CharField(max_length=255,unique=True,blank=True,null=True, verbose_name='Barcode')
    type = models.ForeignKey('MaterialType', models.DO_NOTHING,null=False,verbose_name='Material Type',help_text='for example: Storing Tuna type is Meat, Seafood, and Poultry')
    UOP = models.CharField(max_length=25, choices=MEASURE_UNITS, unique=False, null=False, verbose_name='Unit of Measure Purchase')
    UOC = models.CharField(max_length=25, choices=MEASURE_UNITS, unique=False, null=False, verbose_name='Unit of Measure Consume', help_text='note: Unit of consume will be the unit used to store stock and to move inventory')
    divisibleUOM = models.DecimalField(max_digits=18, decimal_places=2, help_text='For example: Convert from Purchase to Consume unit. In which Unit of Measure material will consume. Further, if bough box of 24pcs, so 24 will be assign here, if consume in box. if each box having item in Kgs, then 24xWeight of each Pcs within carton')
    
    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = (('name', 'internalName'),)


class MaterialType(models.Model):
    type = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = True
###############
# Material > #
###############
