# Generated by Django 4.1 on 2022-08-16 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_purchase_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='quantiles',
            new_name='quantity',
        ),
    ]
