#!/usr/bin/env python3

import os
import sys

from notifications_python_client.notifications import NotificationsAPIClient
from notifications_python_client import prepare_upload


def send_file_by_email():
    if len(sys.argv) == 1:
        print('No arguments passed')
        return

    email_address= sys.argv[1]
    api_key = os.environ["SERVICE_API_KEY"]
    api_host = os.environ["FUNCTIONAL_TESTS_API_HOST"]
    send_file_by_email_template_id = os.environ["SEND_FILE_BY_EMAIL_TEMPLATE_ID"]

    notifications_client = NotificationsAPIClient(api_key, base_url=api_host)

    with open('file_to_send_by_email.pdf', 'rb') as f:
        response = notifications_client.send_email_notification(
            email_address=email_address, # required string
            template_id=send_file_by_email_template_id, # required UUID string
            personalisation={
                "link_to_file": prepare_upload(f)
            }
        )

    print(response)


send_file_by_email()
