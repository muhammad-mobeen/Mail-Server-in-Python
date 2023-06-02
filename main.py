import smtplib
import imaplib
from email.mime.text import MIMEText

with open ("creds.txt", "r") as myfile:
    data = myfile.read().splitlines()

print(data)

# SMTP Server Configuration
SMTP_SERVER = data[0]
SMTP_PORT = int(data[1])

# IMAP Server Configuration
IMAP_SERVER = data[2]
IMAP_PORT = int(data[3])

# Email Credentials
email_user = data[4]
email_password = data[5]


def send_email(recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_user
    msg['To'] = recipient

    # Connect to the SMTP server
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()

    # Login to your Gmail account
    
    smtp_server.login(email_user, email_password)

    # Send the email
    smtp_server.send_message(msg)
    smtp_server.quit()


def receive_emails():
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

    # Login to your Email account
    imap_server.login(email_user, email_password)

    # Select the mailbox (e.g., "INBOX")
    mailbox = 'INBOX'
    imap_server.select(mailbox)

    # Search for emails based on your criteria
    typ, data = imap_server.search(None, 'ALL')

    # Fetch the emails
    for num in data[0].split():
        typ, data = imap_server.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        # Process the raw email as needed
        print(raw_email.decode('utf-8'))

    # Logout and close the connection
    imap_server.logout()


if __name__ == '__main__':

    # Send an email
    send_email('reciever@mail.com', 'Test Subject', 'This is the email body')

    # Receive emails
    receive_emails()

