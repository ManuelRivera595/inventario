# Generated by Django 3.0.8 on 2021-01-04 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210104_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cimal',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
