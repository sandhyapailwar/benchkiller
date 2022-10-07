# Generated by Django 2.1.3 on 2018-11-16 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("crm", "0023_auto_20181116_2252")]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="to_level",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles_to_level",
                to="crm.Level",
            ),
        )
    ]
