import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def verify_mail_send(to_address, name, link):
    msg = MIMEMultipart()
    msg['From'] = "Coin Predict Verification Mail"
    msg['To'] = to_address
    msg['Subject'] = "Verify Your Account."
    body = "Hey {}, " \
           "" \
           "Your Verify Link is {}, Click here to verify your account.".format(name, link)
    msg.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("comradesyndrome@gmail.com", "durgavihar151")
    text = msg.as_string()
    server.sendmail("comradesyndrome@gmail.com", to_address, text)













