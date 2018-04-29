# Generated by Django 2.0.3 on 2018-04-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_auto_20180413_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverytime',
            name='day',
        ),
        migrations.AddField(
            model_name='deliverytime',
            name='evening_day',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deliverytime',
            name='morning_day',
            field=models.IntegerField(default=-1),
        ),
    ]
