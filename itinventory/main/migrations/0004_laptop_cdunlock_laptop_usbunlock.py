# Generated by Django 4.0.2 on 2022-03-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_computer_cdunlock_computer_usbunlock'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='cdunlock',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='laptop',
            name='usbunlock',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
