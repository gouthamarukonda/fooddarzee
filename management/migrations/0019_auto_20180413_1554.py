# Generated by Django 2.0.3 on 2018-04-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_auto_20180413_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergens',
            options={'managed': True, 'verbose_name_plural': 'Allergens'},
        ),
        migrations.AlterModelOptions(
            name='deliveryaddress',
            options={'managed': False, 'verbose_name_plural': 'Delivery Addressess'},
        ),
        migrations.AddField(
            model_name='upgardeplanpricing',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=12),
        ),
    ]
