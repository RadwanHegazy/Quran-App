# Generated by Django 4.0 on 2023-08-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_surah_number_of_ayahs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayah',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='surah',
            name='surah_uid',
            field=models.IntegerField(),
        ),
    ]
