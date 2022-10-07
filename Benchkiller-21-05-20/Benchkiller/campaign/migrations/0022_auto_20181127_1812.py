# Generated by Django 2.1.3 on 2018-11-27 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("campaign", "0021_campaign_aggregate_activities")]

    operations = [
        migrations.CreateModel(
            name="Wave",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="campaign_waves",
                        to="campaign.Campaign",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="activity",
            name="body",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="activity",
            name="subject",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="activity",
            name="campaign",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaign_activity",
                to="campaign.Campaign",
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="wave",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaign_activity",
                to="campaign.Wave",
            ),
        ),
    ]
