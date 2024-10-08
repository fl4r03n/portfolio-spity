# Generated by Django 5.0.4 on 2024-07-17 16:59

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0004_testimonial_testimonialdesc_alter_fact_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="img",
            field=models.ImageField(
                default="about/default.jpg",
                upload_to="about/",
                validators=[core.models.validate_image_size],
                verbose_name="Imagen",
            ),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="testimonial_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="testimonials/",
                validators=[core.models.validate_image_size],
                verbose_name="Imagen del testimonio",
            ),
        ),
    ]
