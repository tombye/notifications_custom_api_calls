# Custom API calls

## Set up

Get yourself a Python virtual environment.

Install dependencies:

`pip install -r requirements.txt`

Copy `environment_template.sh` and set the values yourself.

## Send an inbound message

`./send_inbound_message.py [content of message]`

## Send a file by email

Requires a template to be set up and its id set as an environment variable.

`send_file_by_email.py [email address to send it to]`

## Send an SMS

Requires a phone number to be set as an environment variable.

`./send_sms_from_template.py [template id]`
