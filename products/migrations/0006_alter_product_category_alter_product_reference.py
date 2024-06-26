# Generated by Django 5.0.6 on 2024-06-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('TRP', 'TRP'), ('C50', 'C50'), ('APOLLO', 'APOLLO'), ('G-STREET', 'G-STREET'), ('MINI-JET', 'MINI-JET'), ('CITY', 'CITY'), ('CRUZER', 'CRUZER'), ('ALPHA', 'ALPHA'), ('C100', 'C100'), ('110CC', '110CC'), ('DJ50', 'DJ50'), ('FAME XR', 'FAME XR'), ('FIFTY', 'FIFTY'), ('C90', 'C90'), ('FAME GAMA', 'FAME GAMA'), ('FAME XS', 'FAME XS'), ('S50', 'S50')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='reference',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
