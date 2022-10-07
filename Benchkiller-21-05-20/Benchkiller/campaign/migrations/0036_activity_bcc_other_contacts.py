# Generated by Django 2.1.7 on 2020-05-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0035_contact_display_name'),
        ('campaign', '0035_campaign_bcc'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='bcc_other_contacts',
            field=models.ManyToManyField(blank=True, related_name='bcc_other_contact_activities', to='crm.Contact'),
        ),
    ]
