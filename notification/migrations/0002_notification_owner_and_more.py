# Generated by Django 4.0 on 2022-02-19 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20220206_1951'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('owner', 'id')},
        ),
    ]
