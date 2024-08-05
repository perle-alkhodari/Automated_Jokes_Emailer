import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


class SendMail:

    @staticmethod
    def send_mail(to_user,  subject, msg):
        message = f"Subject:{subject}\n\n{msg}"

        sender = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("APP_PASSWORD")

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()

        connection.login(user=sender, password=sender_password)
        connection.sendmail(to_user, sender, msg=message)

        connection.close()
