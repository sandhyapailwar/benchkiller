# Generated by Django 2.1.3 on 2018-11-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("campaign", "0013_campaign_subject")]

    operations = [
        migrations.AlterField(
            model_name="campaignpredicate",
            name="predicate_field",
            field=models.CharField(
                choices=[
                    ("contact__state", "Contact state"),
                    ("contact_role", "Contact Type"),
                    ("role__location__region", "Region"),
                    ("role__location__country", "Country"),
                    ("role__secondary_skills__name", "Skills"),
                ],
                max_length=255,
                null=True,
            ),
        )
    ]
