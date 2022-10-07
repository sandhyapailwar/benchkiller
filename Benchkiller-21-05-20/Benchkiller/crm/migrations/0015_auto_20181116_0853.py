# Generated by Django 2.1.3 on 2018-11-16 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("crm", "0014_auto_20181114_1211")]

    operations = [
        migrations.RemoveField(model_name="opportunitycontact", name="contacts"),
        migrations.AddField(
            model_name="opportunitycontact",
            name="contacts",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts_opportunity",
                to="crm.Contact",
            ),
        ),
        migrations.RemoveField(model_name="opportunitycontact", name="opportunities"),
        migrations.AddField(
            model_name="opportunitycontact",
            name="opportunities",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="opportunity_contacts",
                to="crm.Opportunity",
            ),
        ),
    ]
