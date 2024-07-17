# Generated by Django 5.0.4 on 2024-07-17 16:59

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_alter_portfolioitem_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolioitem",
            name="image1",
            field=models.ImageField(
                upload_to="portfolio/",
                validators=[core.models.validate_image_size],
                verbose_name="Imagen 1",
            ),
        ),
        migrations.AlterField(
            model_name="portfolioitem",
            name="image2",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="portfolio/",
                validators=[core.models.validate_image_size],
                verbose_name="Imagen 2",
            ),
        ),
        migrations.AlterField(
            model_name="portfolioitem",
            name="image3",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="portfolio/",
                validators=[core.models.validate_image_size],
                verbose_name="Imagen 3",
            ),
        ),
    ]
