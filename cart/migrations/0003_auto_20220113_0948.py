# Generated by Django 3.0.14 on 2022-01-13 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220112_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='date_ordered',
            new_name='date_added',
        ),
    ]
