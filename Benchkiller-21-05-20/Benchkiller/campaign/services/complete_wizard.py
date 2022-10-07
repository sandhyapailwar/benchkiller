from campaign.models.activity import Activity
from campaign.models.campaing_post_action import CampaignPostAction
from django.utils.timezone import now


def email_sent_log(activity: Activity):
    cc = ";".join(map(lambda c: c.email, activity.other_contacts.all()))
    activity.log_line(f'Email was sent to "{activity.contact.email}" cc {cc}')


def set_contact_state(activity: Activity, action: CampaignPostAction) -> None:
    activity.contact.set_state(action.value).save()
    activity.log_line(
        f'Set contact "{activity.contact.full_name}" state to "{action.value}"'
    )
    # for other_contact in activity.other_contacts.all():
    #     other_contact.set_state(action.value).save()


ACTIONS = {CampaignPostAction.FIELD_CONTACT_STATE: set_contact_state}


def execute_action(activity: Activity, action: CampaignPostAction) -> None:
    ACTIONS[action.field](activity, action)


def complete_activity_wizard(activity: Activity) -> None:
    """
    Wizard to automate Activity post processing
    """
    email_sent_log(activity)
    for action in activity.campaign.campaign_post_actions.all():
        execute_action(activity, action)
