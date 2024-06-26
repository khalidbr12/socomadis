# Generated by Django 5.0.6 on 2024-06-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TRP', 'TRP'), ('C50', 'C50'), ('APOLLO', 'APOLLO'), ('G-STREET', 'G-STREET'), ('MINI-JET', 'MINI-JET'), ('CITY', 'CITY'), ('CRUZER', 'CRUZER'), ('ALPHA', 'ALPHA'), ('C100', 'C100'), ('110CC', '110CC'), ('DJ50', 'DJ50'), ('FAME XR', 'FAME XR'), ('FIFTY', 'FIFTY'), ('C90', 'C90'), ('FAME GAMA', 'FAME GAMA'), ('FAME XS', 'FAME XS')], default='TRP', max_length=20),
        ),
    ]