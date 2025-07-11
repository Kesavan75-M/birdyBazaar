# Generated by Django 5.2.4 on 2025-07-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdyapp', '0011_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
