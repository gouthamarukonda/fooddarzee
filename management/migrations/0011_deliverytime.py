# Generated by Django 2.0.3 on 2018-04-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_auto_20180327_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning_time', models.TimeField()),
                ('evening_time', models.TimeField()),
                ('day', models.IntegerField()),
            ],
            options={
                'managed': True,
                'db_table': 'delivery_time',
            },
        ),
    ]
