# Generated by Django 2.1.3 on 2018-11-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("crm", "0021_auto_20181116_2228")]

    operations = [
        migrations.RenameField(
            model_name="contact", old_name="contact_state", new_name="state"
        ),
        migrations.RemoveField(model_name="contact", name="role"),
        migrations.AlterField(
            model_name="contact",
            name="last_name",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
