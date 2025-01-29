#!/usr/bin/env python3

import os
import sys

from notifications_python_client.notifications import NotificationsAPIClient


def get_notification_by_id():
    if len(sys.argv) == 1:
        print('No arguments passed, you need to pass the notification id')

    notification_id = sys.argv[1]
    api_key = os.environ["SERVICE_API_KEY"]
    api_host = os.environ["FUNCTIONAL_TESTS_API_HOST"]

    notifications_client = NotificationsAPIClient(api_key, base_url=api_host)

    response = notifications_client.get_notification_by_id(notification_id)

    print(response)


get_notification_by_id()
