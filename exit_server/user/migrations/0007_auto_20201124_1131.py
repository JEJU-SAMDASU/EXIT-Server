# Generated by Django 3.1.3 on 2020-11-24 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201124_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
