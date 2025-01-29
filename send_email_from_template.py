#!/usr/bin/env python3

import os
import sys

from notifications_python_client.notifications import NotificationsAPIClient


def send_email_from_template():
    if len(sys.argv) == 1:
        print('No arguments passed, you need to pass the template_id and the email address to send to')
        return
    if len(sys.argv) == 2:
        print('Not enough arguments passed, you need to pass the template_id and the email address to send to')
        return

    template_id = sys.argv[1]
    email_address = sys.argv[2]
    api_key = os.environ["SERVICE_API_KEY"]
    api_host = os.environ["FUNCTIONAL_TESTS_API_HOST"]

    notifications_client = NotificationsAPIClient(api_key, base_url=api_host)

    response = notifications_client.send_email_notification(
        email_address=email_address,
        template_id=template_id,
    )

    print(response)


send_email_from_template()
