# Generated by Django 2.2.19 on 2022-04-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20220425_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code_iso',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Код ISO'),
        ),
    ]
