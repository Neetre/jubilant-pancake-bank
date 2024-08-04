import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import ssl
import os

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('EMAIL_PASSWORD')

# 465 SSL
# 587 TSL

def smtp_server(email):
    domain = email.split("@")[1]
    domain = "smtp." + domain
    return domain


def send_email(to_email: str, subject: str, body: str, filepath: str = None):
    SMTP_SERVERS = smtp_server(to_email)

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(SMTP_SERVERS, 465, context=context)
    server.login(EMAIL, PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        elif not os.path.isfile(filepath):
            raise ValueError(f"Path is not a file: {filepath}")
        elif filepath is not None:
            filepath = filepath
            filename = os.path.basename(filepath)
            attachment = open(filepath, 'rb')
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(p)

    except Exception as e:
        print(f"Exception cought while reading filepath: {e}")

    text = msg.as_string()
    server.sendmail(EMAIL, to_email, text)


if __name__ == "__main__":
    send_email("test@icloud.com", "Hello", "Little trolling")
