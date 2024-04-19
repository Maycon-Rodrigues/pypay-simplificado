# Generated by Django 5.0.4 on 2024-04-17 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                    "person_type",
                    models.CharField(
                        choices=[("C", "COMMON"), ("S", "SHOPKEEPER")],
                        default="C",
                        max_length=1,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("document", models.CharField(max_length=100, unique=True)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "payee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="payee",
                        to="api.person",
                    ),
                ),
                (
                    "payer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="payer",
                        to="api.person",
                    ),
                ),
            ],
        ),
    ]