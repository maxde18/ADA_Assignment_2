from twilio.rest import Client

account_sid = 'AC851b4c1508639e4b538bcd58051d682b'
auth_token = 'c99627017eeaca5342c6647f5e986853'


def send_sms(user_numbers):

  client = Client(account_sid, auth_token)

  for number in user_numbers:
    message = client.messages.create(
      from_='+19123944524',
      body='Changes or announcements have been made for a festival you have tickets for, check the website for more details',
      to=number
  )
    print(message.sid)


