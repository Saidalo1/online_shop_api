# Generated by Django 4.1.3 on 2023-02-08 12:19

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='details',
            field=django.contrib.postgres.fields.hstore.HStoreField(default=dict, verbose_name='details of product'),
        ),
    ]