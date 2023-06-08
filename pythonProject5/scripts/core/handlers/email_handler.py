import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schemas.models import Email
from scripts.constants.emailcons import email_obj
from scripts.core.handlers import Item_handler


def send_email(email: Email):
    # Set up the email details
    sender_email = email_obj.sender_email
    sender_password = email_obj.sender_password
    receiver_email = email.rec_email

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject

    # Add the body to the email
    message.attach(MIMEText(email.body, "plain"))
    count_books = Item_handler.read_item()
    str_count = str(count_books)
    message.attach(MIMEText("Total number of items: \n" + str_count))

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # Login to the sender's email account
        server.login(sender_email, sender_password)
        # Send the email
        server.send_message(message)
        # Close the connection
        server.quit()
        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}
