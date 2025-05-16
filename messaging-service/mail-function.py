from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content, Personalization


def send_mail(recipients):

    sg = SendGridAPIClient(api_key='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')
    from_email = Email('maxrobertdl@gmail.com')
    subject = 'Updates on your festival(s)'
    content = Content('text/html','<strong>One of your festivals have updates, check the FestiFlow website for more info!</strong>')

    mail = Mail()
    mail.from_email = from_email
    mail.subject = subject
    mail.add_content(content)

    for recipient_email  in recipients:
        personalization = Personalization()
        personalization.add_to(Email(recipient_email))  # Use Email instead of To here
        mail.add_personalization(personalization)

    # Send the email
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print("Error sending email:", str(e))