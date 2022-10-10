# Generated by Django 4.0.7 on 2022-10-09 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Material Name')),
                ('internalName', models.CharField(help_text='i.e (milk, egg, chicken, tuna) in respective unit', max_length=255, verbose_name='Material Internal Name')),
                ('barcode', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Barcode')),
                ('UOP', models.CharField(choices=[('Kilogram', 'Kilogram'), ('Gram', 'Gram'), ('Milligram', 'Milligram'), ('Litre', 'Litre'), ('Pint', 'Pint'), ('Millilitre', 'Millilitre'), ('Tablespoon', 'Tablespoon'), ('Teaspoon', 'Teaspoon'), ('Box', 'Box'), ('Carton', 'Carton'), ('Pc', 'Pc'), ('Dozen', 'Dozen'), ('Bottle', 'Bottle')], max_length=25, verbose_name='Unit of Measure Purchase')),
                ('UOC', models.CharField(choices=[('Kilogram', 'Kilogram'), ('Gram', 'Gram'), ('Milligram', 'Milligram'), ('Litre', 'Litre'), ('Pint', 'Pint'), ('Millilitre', 'Millilitre'), ('Tablespoon', 'Tablespoon'), ('Teaspoon', 'Teaspoon'), ('Box', 'Box'), ('Carton', 'Carton'), ('Pc', 'Pc'), ('Dozen', 'Dozen'), ('Bottle', 'Bottle')], help_text='note: Unit of consume will be the unit used to store stock and to move inventory', max_length=25, verbose_name='Unit of Measure Consume')),
                ('packingOf', models.DecimalField(decimal_places=2, help_text='For example: Convert from Purchase to Consume unit.In which Unit of Measure material will consume. Further, if bough box of 24pcs, so 24 will be assign here, if consume in box. if each box having item in Kgs, then 24xWeight of each Pcs within carton', max_digits=18)),
                ('howMany', models.DecimalField(decimal_places=2, help_text='Important: If Purchase unit and sale units are not same, than provide unit of consumtion quantity/weights', max_digits=18)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='for example: Storing Tuna type is Meat, Seafood, and Poultry', max_length=50, unique=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardEnding', models.CharField(default='Cash', help_text='Ending 4 digit of card used or Cash etc...', max_length=50, unique=True, verbose_name='Card Number / Cash')),
                ('name', models.CharField(default='Cash', help_text='i.e(Shariq Halifax, MPhenom NatWest, Rasa Cash, TripleOne Cash)', max_length=50, unique=True, verbose_name='Owner/Holder Name')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_doc_no', models.IntegerField()),
                ('docType', models.CharField(choices=[('GRN', 'GRN'), ('Return', 'Return'), ('Transfer', 'Transfer'), ('Wastage', 'Wastage')], max_length=15)),
                ('doc_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Warehouse Name')),
                ('whtype', models.CharField(choices=[('Frozen', 'Frozen'), ('Cold', 'Cold'), ('Dry', 'Dry'), ('Misc.', 'Misc.')], help_text='describe, is it consider COLD, Misc, Frozen...', max_length=25, verbose_name='Warehouse Type')),
                ('location', models.CharField(blank=True, default='N/A', help_text='describe where it is stack.', max_length=50, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='StoreDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('increase_qty', models.DecimalField(decimal_places=2, max_digits=18)),
                ('decrease_qty', models.DecimalField(decimal_places=2, max_digits=18)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MM.store')),
                ('itemName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MM.materialmaster')),
            ],
        ),
        migrations.AddField(
            model_name='materialmaster',
            name='type',
            field=models.ForeignKey(help_text='for example: Storing Tuna type is Meat, Seafood, and Poultry', on_delete=django.db.models.deletion.DO_NOTHING, to='MM.materialtype', verbose_name='Material Type'),
        ),
        migrations.AddField(
            model_name='materialmaster',
            name='warehouse',
            field=models.ForeignKey(help_text='Where it is store, internaly after inward', on_delete=django.db.models.deletion.DO_NOTHING, to='MM.warehouse', verbose_name='Where it Store / Warehouse'),
        ),
        migrations.CreateModel(
            name='GrnNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNumber', models.CharField(max_length=50, verbose_name='Supplier / Vendor Invoice number')),
                ('vendorName', models.CharField(max_length=60, verbose_name='Supplier/Vendor Name')),
                ('date', models.DateTimeField(verbose_name='Date of Invoice')),
                ('isPosted', models.BooleanField(default=False)),
                ('note', models.CharField(blank=True, default='N/A', max_length=100)),
                ('time_stamp', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MM.paymentmethods')),
            ],
        ),
        migrations.CreateModel(
            name='GrnItemsDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irate', models.DecimalField(decimal_places=2, max_digits=18)),
                ('iqty', models.DecimalField(decimal_places=2, max_digits=18)),
                ('grn_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MM.grnnote')),
                ('itemName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MM.materialmaster')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='materialmaster',
            unique_together={('internalName', 'UOC'), ('name', 'internalName')},
        ),
    ]
