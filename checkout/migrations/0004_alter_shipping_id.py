# Generated by Django 4.0 on 2022-02-03 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220119_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]