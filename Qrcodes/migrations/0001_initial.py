# Generated by Django 4.1.7 on 2024-12-21 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clientqrcode",
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
                ("nom", models.CharField(max_length=100)),
                ("prenoms", models.CharField(max_length=100)),
                ("date_naissance", models.DateField()),
                ("adresse", models.CharField(max_length=200)),
                ("numero_cni", models.CharField(max_length=50, unique=True)),
                ("telephone", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="QR_code",
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
                ("data", models.CharField(max_length=255)),
                (
                    "qr_code",
                    models.ImageField(blank=True, null=True, upload_to="qr_code/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attestation",
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
                    "type_attestation",
                    models.CharField(
                        choices=[
                            ("cession", "Attestation de Cession"),
                            ("villageoise", "Attestation Villageoise"),
                        ],
                        max_length=50,
                    ),
                ),
                ("numero", models.CharField(editable=False, max_length=9, unique=True)),
                ("lot_numero", models.CharField(max_length=50)),
                ("superficie", models.DecimalField(decimal_places=2, max_digits=10)),
                ("lotissement", models.CharField(max_length=255)),
                ("arrete_reference", models.CharField(max_length=255)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Qrcodes.clientqrcode",
                    ),
                ),
            ],
            options={
                "unique_together": {("lot_numero", "lotissement")},
            },
        ),
    ]
