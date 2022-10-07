# Generated by Django 2.1.7 on 2020-05-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0035_contact_display_name'),
        ('campaign', '0036_activity_bcc_other_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='bcc_other_contacts',
        ),
        migrations.AddField(
            model_name='activity',
            name='bcc_contacts',
            field=models.ManyToManyField(blank=True, related_name='bcc_contacts_activities', to='crm.Contact'),
        ),
    ]