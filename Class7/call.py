# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACb61a4deb059285cf924aa4ae147f43b6'
auth_token = '0a544422bce10ac5cde63bc24e535db3'
client = Client(account_sid, auth_token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to='+8801735774127',
    from_='+18043125076'
)

print(call.sid)
