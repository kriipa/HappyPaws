# Generated by Django 3.0.14 on 2022-02-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_shipping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
