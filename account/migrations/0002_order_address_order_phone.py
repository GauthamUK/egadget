# Generated by Django 4.2.3 on 2023-08-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
