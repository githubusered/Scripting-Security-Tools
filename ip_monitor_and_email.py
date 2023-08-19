import smtplib
import socket
import os.path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
smtp_port = 587  # Port for TLS
sender_email = 'test_sendermail'
receiver_email = 'test_receivermail'
subject = 'Test Email'
message_body = 'This is a test email sent using Python.'

# Create the MIME message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message_body, 'plain'))

# Connect to the Gmail SMTP server and send the email
try:
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()  # Start TLS encryption
    smtp.login(sender_email, 'test_password')  # Use the app-specific password
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully.')
except (smtplib.SMTPException, socket.error) as e:
    print(f'An error occurred: {e}')
finally:
    smtp.quit()
