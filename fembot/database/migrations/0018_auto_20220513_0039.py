# Generated by Django 2.2.19 on 2022-05-12 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_auto_20220507_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['country', 'section', 'id'], 'verbose_name': 'Шаг', 'verbose_name_plural': 'Шаги'},
        ),
    ]
