# Generated by Django 5.0.7 on 2024-08-13 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_category_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['sort'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['sort'], 'verbose_name_plural': 'Dishes'},
        ),
    ]
