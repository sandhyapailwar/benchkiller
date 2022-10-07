import tempfile
import random
import string
import argparse

from agent.utils.agent_mailing import (
    get_activities_list,
    get_attachment,
    mark_activity_as_in_progress,
    mark_activity_as_sent,
    send_mail_via_com,
)


def main(**kwargs):
    recipient = kwargs.get("recipient")
    with tempfile.TemporaryDirectory() as tmpdir:
        activities = get_activities_list()
        sent = 0
        for activity in activities:
            mark_activity_as_in_progress(activity_id=activity["id"])
            attachments = get_attachment(activity, tmpdir)
            # hash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
            subject = activity["subject"]
            recipient_to = recipient if recipient else activity["contact"]["email"]
            recipient_cc = (
                None
                if recipient
                else ";".join([c["email"] for c in activity["other_contacts"]])
            )
            recipient_bcc = (
                None
                if recipient
                else ";".join([bc["email"] for bc in activity["bcc_contacts"]])
            )
            send_mail_via_com(
                subject=subject,
                recipient_to=recipient_to,
                recipient_cc=recipient_cc,
                recipient_bcc=recipient_bcc,
                attachments=attachments,
                text=activity["body"],
                html_text=activity["html_body"],
            )
            mark_activity_as_sent(activity_id=activity["id"])
            sent += 1
        print(f"ALL MAIL SENT: {sent}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spambot Mailer Agent")
    parser.add_argument("-r", "--recipient", dest="recipient")
    args = parser.parse_args()
    params = vars(args)
    main(**params)
