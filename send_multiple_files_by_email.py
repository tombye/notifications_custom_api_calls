#!/usr/bin/env python3

import os
import sys

from notifications_python_client.notifications import NotificationsAPIClient
from notifications_python_client import prepare_upload

# Before this will work, you need to enable "Send files by email", on your service, under "settings".

def send_multiple_files_by_email():
    if len(sys.argv) < 4:
        print('Error: Incorrect number of arguments')
        print('Usage: python send_multiple_files_by_email.py email@example.com file1 file2')
        sys.exit(1)

    email_address = sys.argv[1]
    file_1 = sys.argv[2]
    file_2 = sys.argv[3]
    api_key = os.environ["SERVICE_API_KEY"]
    api_host = os.environ["FUNCTIONAL_TESTS_API_HOST"]
    send_file_by_email_template_id = os.environ["SEND_TWO_FILES_BY_EMAIL_TEMPLATE_ID"]

    notifications_client = NotificationsAPIClient(api_key, base_url=api_host)

    files_to_send = [file_1, file_2]

    personalisation_data = {}

    for index, file_path in enumerate(files_to_send, start=1):
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                # Creates keys like "link_to_file_1", "link_to_file_2" which need to be in the template.
                placeholder_key = f"link_to_file_{index}"
                personalisation_data[placeholder_key] = prepare_upload(f)
        else:
            print(f"Warning: {file_path} not found. Skipping.")

    if personalisation_data:
        response = notifications_client.send_email_notification(
            email_address=email_address,
            template_id=send_file_by_email_template_id,
            personalisation=personalisation_data
        )
        print(response)
    else:
        print("Error: No files were successfully prepared. Email not sent.")


if __name__ == "__main__":
    send_multiple_files_by_email()
