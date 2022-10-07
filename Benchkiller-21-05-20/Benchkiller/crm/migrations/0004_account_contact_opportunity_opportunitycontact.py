# Generated by Django 2.1.3 on 2018-11-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crm", "0003_auto_20181108_1206")]

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("state", models.CharField(max_length=30)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=30)),
                ("role", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Opportunity",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="OpportunityContact",
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
                ("project_role", models.CharField(max_length=20)),
                (
                    "contacts",
                    models.ManyToManyField(
                        blank=True, related_name="contacts", to="crm.Contact"
                    ),
                ),
                (
                    "opportunities",
                    models.ManyToManyField(
                        blank=True, related_name="opportunities", to="crm.Opportunity"
                    ),
                ),
            ],
        ),
    ]