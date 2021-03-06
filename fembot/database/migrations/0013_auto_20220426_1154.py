# Generated by Django 2.2.19 on 2022-04-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_remove_step_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='admin_name',
        ),
        migrations.AddField(
            model_name='country',
            name='name_rus',
            field=models.CharField(default='страна', max_length=20, verbose_name='Название на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='country',
            name='name_ukr',
            field=models.CharField(default='cnhfyf_erh', max_length=20, verbose_name='Название на украинском'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CountryName',
        ),
    ]
