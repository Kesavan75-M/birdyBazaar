# Generated by Django 5.2.4 on 2025-07-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdyapp', '0006_birdproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birdproduct',
            name='age',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='birdproduct',
            name='weight',
            field=models.CharField(max_length=20),
        ),
    ]
