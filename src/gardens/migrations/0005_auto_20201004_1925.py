# Generated by Django 3.1 on 2020-10-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0004_auto_20201004_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='name',
            field=models.CharField(default='defaultValue', max_length=100),
            preserve_default=False,
        ),
    ]
