# Generated by Django 4.0 on 2021-12-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ticker',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
