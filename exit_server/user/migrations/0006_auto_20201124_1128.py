# Generated by Django 3.1.3 on 2020-11-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201124_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subject',
            field=models.CharField(default='진로', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='category',
            field=models.ManyToManyField(to='user.Category'),
        ),
    ]
