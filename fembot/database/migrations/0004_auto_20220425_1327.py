# Generated by Django 2.2.19 on 2022-04-25 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20220425_1245'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='countryname',
            unique_together={('country', 'language')},
        ),
    ]