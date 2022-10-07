# Generated by Django 2.1.3 on 2018-11-09 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("crm", "0003_auto_20181108_1206")]

    operations = [
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("number", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("region", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("role", models.CharField(max_length=200)),
                ("requirements", models.TextField()),
                ("state", models.CharField(max_length=200)),
                ("valid_from", models.DateTimeField(verbose_name="date valid from")),
                ("valid_till", models.DateTimeField(verbose_name="date valid till")),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crm.Location"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                (
                    "skillrole",
                    models.ManyToManyField(
                        blank=True, related_name="roles", to="crm.Role"
                    ),
                ),
            ],
        ),
    ]
