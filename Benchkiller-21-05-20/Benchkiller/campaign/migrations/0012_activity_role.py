# Generated by Django 2.1.3 on 2018-11-20 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0027_auto_20181120_1237"),
        ("campaign", "0011_auto_20181120_1257"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="role_activities",
                to="crm.Role",
            ),
        )
    ]
