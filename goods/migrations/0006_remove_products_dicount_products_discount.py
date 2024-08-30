# Generated by Django 5.0.6 on 2024-08-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_remove_products_discount_products_dicount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='dicount',
        ),
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, null=True, verbose_name='Скидка в %'),
        ),
    ]
