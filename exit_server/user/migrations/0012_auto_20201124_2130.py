# Generated by Django 3.1.3 on 2020-11-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20201124_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abletime',
            name='able_from',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='abletime',
            name='able_to',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
