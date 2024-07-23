from datetime import datetime
from urllib.parse import quote_plus

import requests


def send_inbound_sms(message):
    user_number = os.environ["TEST_NUMBER"]
    service_inbound_number = os.environ["FUNCTIONAL_TESTS_SERVICE_INBOUND_NUMBER"]
    notify_api_url = os.environ["FUNCTIONAL_TESTS_API_HOST"]

    # hand-craft a request to receive messages API.
    mmg_inbound_body = {
        "MSISDN": user_number,
        "Number": service_inbound_number,
        "Message": quote_plus(message),
        "ID": "SOME-MMG-SPECIFIC-ID",
        "DateRecieved": quote_plus(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")),
    }

    response = requests.post(
        notify_api_url + "/notifications/sms/receive/mmg",
        json=mmg_inbound_body,
        auth=(
            os.environ["MMG_INBOUND_SMS_USERNAME"],
            os.environ["MMG_INBOUND_SMS_AUTH"],
        ),
    )

    print(response)

    print(response.raise_for_status())
