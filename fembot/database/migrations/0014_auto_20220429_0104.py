# Generated by Django 2.2.19 on 2022-04-28 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20220426_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['country', 'section', 'changed'], 'verbose_name': 'Шаг', 'verbose_name_plural': 'Шаги'},
        ),
    ]
