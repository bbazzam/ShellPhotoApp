import random
import vlc
import logging
import time

from os import listdir
from os.path import isfile, join
from random import randrange, uniform
from datetime import datetime

class EmailClient:

   def __init__(self):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.loadEmailClient()

   def loadEmailClient(self):
      self.log.info("Loading Email Client")

      return

   def sendPicture(self, picture):
       self.log.info("Emailing Picture %s",  picture)
       return




# https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
# import email, smtplib, ssl

# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# subject = "An email with attachment from Python"
# body = "This is an email with attachment sent from Python"
# sender_email = "my@gmail.com"
# receiver_email = "your@gmail.com"
# password = input("Type your password and press enter:")

# # Create a multipart message and set headers
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = subject
# message["Bcc"] = receiver_email  # Recommended for mass emails

# # Add body to email
# message.attach(MIMEText(body, "plain"))

# filename = "document.pdf"  # In same directory as script

# # Open PDF file in binary mode
# with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())

# # Encode file in ASCII characters to send by email    
# encoders.encode_base64(part)

# # Add header as key/value pair to attachment part
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )

# # Add attachment to message and convert message to string
# message.attach(part)
# text = message.as_string()

# # Log in to server using secure context and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, text)