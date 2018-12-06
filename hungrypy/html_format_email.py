import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "youremail@email.com"
password = "yourpassword"
from_email = username
to_list = ["receiver_emai@email.com"]

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    email_conn.sendmail(from_email, "Hello there...")
    email_conn.quit()

    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello there!"
    the_msg['From'] = from_email
    # the_msg['To'] = to_list

    plain_txt = "Testing the message"
    html_txt = """\
    <html>
        <head></head>
        <body>
        <p>Hey!<br>
        Testing this email <b> Message</b>. Made by <a href="http://somelink.com">Team </a>
        </p>
        </body>
    </html>
    """

    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(from_email, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("Error sending message")
