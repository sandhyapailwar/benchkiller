from operator import attrgetter
from jinja2 import Template
from campaign.models.activity import Activity
from campaign.models.activity_opportunities import ActivityOpportunityContact
from campaign.models.campaign import Campaign
from campaign.models.wave import Wave
from campaign.services.predicate_builder import contact_iterator_builder
from crm.models.contact import Contact
from crm.models.opportunitycontact import OpportunityContact


def wave_wizard(request: any, campaign: Campaign) -> None:
    activities = list()
    wave = Wave.objects.create(campaign=campaign)
    subject_template = Template(campaign.subject)
    body_template = Template(campaign.template) if campaign.template else None
    html_body_template = (
        Template(campaign.html_template) if campaign.html_template else None
    )

    for opportunity_contact in contact_iterator_builder(campaign):
        activity = wave_create_activity(
            wave, opportunity_contact, update=campaign.aggregate_activities
        )
        activities.append(activity)

    for activity in activities:
        ctx = dict(
            contact=activity.contact,
            campaign=activity.campaign,
            wave=activity.wave,
            opportunity_contacts=list(
                map(
                    attrgetter("opportunity_contact"),
                    activity.activity_opportunity_contacts.all(),
                )
            ),
            roles=list(set(
                map(attrgetter("role"), activity.activity_opportunity_contacts.all()))
            ),
            opportunities=list(
                map(
                    attrgetter("opportunity"),
                    activity.activity_opportunity_contacts.all(),
                )
            ),
            custom=dict(),
        )

        if activity.activity_opportunity_contacts.count() == 1:
            activity_opportunity_contact: ActivityOpportunityContact = activity.activity_opportunity_contacts.first()
            opportunity_contact = activity_opportunity_contact.opportunity_contact
            ctx.update(
                opportunity_contact=opportunity_contact,
                role=opportunity_contact.role,
                opportunity=opportunity_contact.opportunity,
            )
        else:
            ctx.update(opportunity_contact=None, role=None, opportunity=None)

        for prop in campaign.campaign_properties.all():
            if "{{" in prop.value:
                _tpl = Template(prop.value)
                try:
                    ctx["custom"][prop.name] = _tpl.render(**ctx)
                except:
                    raise Exception(f'Failed to assing {prop.name} with {ctx}')
            else:
                ctx["custom"][prop.name] = prop.value


        activity.subject = subject_template.render(**ctx)
        activity.body = body_template.render(**ctx) if body_template else None
        activity.html_body = (
            html_body_template.render(**ctx) if html_body_template else None
        )

        assert activity.body or activity.html_body

        activity.save()


def wave_create_activity(
    wave: Wave, opportunity_contact: OpportunityContact, **kwargs
) -> Activity:
    contact: Contact = kwargs.get("contact", opportunity_contact.contact)
    update: bool = bool(kwargs.get("update"))

    activity_params = dict(campaign=wave.campaign, wave=wave, contact=contact)

    if not update:
        activity = Activity.objects.create(**activity_params)
        for cc in wave.campaign.cc.all():
            activity.other_contacts.add(cc)
        for bcc in wave.campaign.bcc.all():
            activity.bcc_contacts.add(bcc)
    else:
        activity, created = Activity.objects.get_or_create(**activity_params)
        activity.other_contacts.remove()
        activity.bcc_contacts.remove()
        for cc in wave.campaign.cc.all():
            activity.other_contacts.add(cc)
        for bcc in wave.campaign.bcc.all():
            activity.bcc_contacts.add(bcc)

    ActivityOpportunityContact.objects.create(
        opportunity_contact=opportunity_contact,
        activity=activity,
        opportunity=opportunity_contact.opportunity,
        role=opportunity_contact.role,
        contact_role=opportunity_contact.contact_role,
    )

    return activity
