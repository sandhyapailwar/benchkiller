# Generated by Django 2.1.3 on 2018-11-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("etl", "0002_auto_20181120_0633")]

    operations = [
        migrations.AlterField(
            model_name="etltask",
            name="log",
            field=models.TextField(editable=False, null=True),
        )
    ]