# Generated by Django 5.1.4 on 2024-12-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicies',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
