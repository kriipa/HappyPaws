# Generated by Django 3.0.14 on 2022-02-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
