# Generated by Django 3.2.4 on 2022-05-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_area_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='imagen',
            field=models.ImageField(null=True, upload_to='areas'),
        ),
    ]
