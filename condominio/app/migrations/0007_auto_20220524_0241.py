# Generated by Django 3.2.4 on 2022-05-24 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220524_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago_estado',
            name='forma_pago',
        ),
        migrations.RemoveField(
            model_name='pago_reserva',
            name='forma_pago',
        ),
    ]
