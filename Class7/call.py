# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'YOUR SID'
auth_token = 'YOUR AUTH TOKEN'
client = Client(account_sid, auth_token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to='+8801735774127',
    from_='+18043125076'
)

print(call.sid)
