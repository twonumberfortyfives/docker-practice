# Generated by Django 5.0.6 on 2024-05-21 19:26

import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.upload_image),
        ),
    ]