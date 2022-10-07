from campaign.models.campaign import Campaign
from campaign.models.campaign_predicate import CampaignPredicate
from crm.models.opportunitycontact import OpportunityContact


def build_predicate(queryset: any, predicate: CampaignPredicate) -> any:
    if predicate.inverse:
        filter_fn = queryset.exclude
    else:
        filter_fn = queryset.filter

    condition = predicate.predicate_field + predicate.predicate_condition
    return filter_fn(**{condition: predicate.predicate_value})


def contact_iterator_builder(campaign: Campaign) -> any:
    contacts = OpportunityContact.objects
    predicates = campaign.campaign_predicates.filter(active__exact=True)

    if not predicates:
        contacts = contacts.all()
    else:
        for predicate in predicates:
            contacts = build_predicate(contacts, predicate)

    return contacts
