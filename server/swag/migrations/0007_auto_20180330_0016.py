# Generated by Django 2.0.2 on 2018-03-29 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swag', '0006_auto_20180122_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='load_value',
            field=models.FloatField(null=True),
        ),
    ]