# Generated by Django 5.0.4 on 2024-07-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "icon_name",
                    models.CharField(
                        default="youtube",
                        help_text="Nombre del ícono (ej. youtube). Visita https://boxicons.com para ver la lista completa de íconos.",
                        max_length=50,
                    ),
                ),
                (
                    "icon_color",
                    models.CharField(
                        default="darkred",
                        help_text="Color del ícono (ej. blue, red, yellow). Usa colores válidos en CSS.Visita https://www.w3schools.com/cssref/css_colors.php para ver la lista completa de colores.",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "verbose_name": "Servicio",
                "verbose_name_plural": "Servicios",
            },
        ),
        migrations.CreateModel(
            name="ServicesDesc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tittle_section",
                    models.CharField(
                        default="Services",
                        max_length=100,
                        verbose_name="Título de Sección",
                    ),
                ),
                (
                    "desc_section",
                    models.TextField(
                        default="Magnam dolores commodi suscipit...",
                        verbose_name="Descripción de Sección",
                    ),
                ),
            ],
            options={
                "verbose_name": "Descripcion de Servicios",
                "verbose_name_plural": "Descripciones de Servicios",
            },
        ),
    ]
