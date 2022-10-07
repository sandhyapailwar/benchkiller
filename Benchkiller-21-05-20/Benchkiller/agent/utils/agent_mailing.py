from os import path
import requests
from jinja2 import Template
import win32com.client


def message_builder():
    o = win32com.client.Dispatch("Outlook.Application")
    print(dir(o))
    return o.CreateItem(0)


def send_mail_via_com(
    subject, recipient_to, recipient_cc, recipient_bcc, attachments, text, html_text=None
):
    msg = message_builder()
    msg.Importance = 0
    msg.Subject = subject
    msg.GetInspector  # to add signature

    if html_text:
        msg.Body = text
        msg.HTMLBody = html_text
    else:
        index = msg.HTMLBody.find(">", msg.HTMLBody.find("<body"))
        msg.HTMLBody = msg.HTMLBody[: index + 1] + text + msg.HTMLBody[index + 1 :]
        msg.Body = text

    #
    for attachment in attachments:
        msg.Attachments.Add(attachment)

    msg.To = recipient_to

    if recipient_cc:
        msg.CC = recipient_cc

    if recipient_bcc:
        msg.BCC = recipient_bcc


    # msg.Display()
    msg.Send()


def get_activities_list():
    activities_list = list()
    activities = requests.get("http://localhost:8001/api/v1/activity?state=new").json()
    for activity in activities:
        activities_list.append(activity)
    return activities_list


def mark_activity_as_sent(activity_id):
    result = requests.get(
        f"http://localhost:8001/api/v1/activity/{activity_id}/sent/",
        headers={"Content-Type": "application/json"},
    )


def mark_activity_as_in_progress(activity_id):
    result = requests.get(
        f"http://localhost:8001/api/v1/activity/{activity_id}/in_progress/",
        headers={"Content-Type": "application/json"},
    )


def get_attachment(activity, tmp_dir):
    attachments = activity["attachments"]
    files = list()
    for attachment in attachments:
        url = attachment["attachment"]
        file_name = path.join(tmp_dir, url.split("/")[-1])
        files.append(file_name)
        r = requests.get(url)
        with open(file_name, "wb") as f:
            f.write(r.content)
    return files
