# Generated by Django 4.2.6 on 2023-10-20 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebSiteApp', '0003_rename_total_rental_book_total_renta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='total_renta',
            new_name='total_rental',
        ),
    ]
