# Generated by Django 2.1.3 on 2018-11-28 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("campaign", "0024_auto_20181128_0804")]

    operations = [
        migrations.RenameField(
            model_name="activityopportunitycontact",
            old_name="opportunty_contact",
            new_name="opportunity_contact",
        )
    ]