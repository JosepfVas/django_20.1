# Generated by Django 5.0.3 on 2024-04-06 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
