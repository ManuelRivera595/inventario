# Generated by Django 3.0.8 on 2021-01-04 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_cimal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cimal',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]