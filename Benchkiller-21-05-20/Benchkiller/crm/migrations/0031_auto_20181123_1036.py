# Generated by Django 2.1.3 on 2018-11-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crm", "0030_auto_20181123_1011")]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="secondary_skills",
            field=models.TextField(blank=True, default=None, null=True),
        )
    ]
