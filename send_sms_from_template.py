#!/usr/bin/env python3

import os
import sys

from notifications_python_client.notifications import NotificationsAPIClient


def send_sms_from_template():
    if len(sys.argv) == 1:
        print('No arguments passed')
        return

    template_id = sys.argv[1]
    api_key = os.environ["SERVICE_API_KEY"]
    api_host = os.environ["FUNCTIONAL_TESTS_API_HOST"]
    test_number = os.environ["TEST_NUMBER"]

    notifications_client = NotificationsAPIClient(api_key, base_url=api_host)

    response = notifications_client.send_sms_notification(
        phone_number=test_number,
        template_id=template_id,
    )

    print(response)


send_sms_from_template()
