#'''
 # @ Author: Ben Azzam
 # @ Create Time: 2021-09-24 23:45:52
 # @ Modified by: Ben Azzam
 # @ Modified time: 2021-09-25 00:38:01
 # @ Description:
 # With support from
 # https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development
 #'''

from email import message
import random
import vlc
import logging
import time
import email, smtplib, ssl
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import listdir
from os.path import isfile, join
from random import randrange, uniform
from datetime import datetime

class EmailClient:

   def __init__(self):
      self.log = logging.getLogger(__name__ + '.' + self.__class__.__name__)
      self.log.info("Loading Email Client")
      self.subject = "New Photo Alert"
      self.body = "Look who we caught pushing the don't push button"
      self.sender_email = os.environ.get('SENDER_EMAIL')
      self.receiver_email = os.environ.get('RECEIVER_EMAIL')
      self.password = os.environ.get('EMAIL_PWD')

   def sendPicture(self, picture):
       self.log.info("Emailing Picture %s",)
       message = self.createMessage(picture)
       self.sendMessage(message)
       return

   def createMessage(self, file):
      # Create a multipart message and set headers
      message = MIMEMultipart()
      message["From"] = self.sender_email
      message["To"] = self.receiver_email
      message["Subject"] = self.subject
      message["Bcc"] = self.receiver_email  # Recommended for mass emails
      # # Add body to email
      self.body = self.body + "\n photo:" + file
      message.attach(MIMEText(self.body, "plain"))
      # # Open image file in binary mode
      with open(file, "rb") as attachment:
      #     # Add file as application/octet-stream
      #     # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

      # Encode file in ASCII characters to send by email    
      encoders.encode_base64(part)

      # Add header as key/value pair to attachment part
      part.add_header(
         "Content-Disposition",
         f"attachment; filename= {file}",
      )

      # Add attachment to message and convert message to string
      message.attach(part)
      return message

   def sendMessage(self, message):
      text = message.as_string()
      try:
      # Log in to server using secure context and send email
         context = ssl.create_default_context()
         self.log.info("Sending image subject %s to %s from %s ", message.get("Subject"), self.sender_email, self.receiver_email)
         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, text)
      except:
        self.log.exception("Issue with emailing picture ", message.get("Subject"))
