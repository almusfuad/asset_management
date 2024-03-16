# Generated by Django 5.0.3 on 2024-03-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[('Phone', 'Phone'), ('Tablet', 'Tablet'), ('Laptop', 'Laptop'), ('Other Gear', 'Other Gear')], max_length=50),
        ),
    ]