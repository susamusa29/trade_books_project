#Abrar Haroon
#configuration settings for email

import smtplib
import os

from email.message import EmailMessage

#Config.py contains sensitive data about the email address used to send confirmation
EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_SUBJECT = 'Order Confirmation'
EMAIL_MESSAGE = 'This message is to confirm that your order is complete. \nContact the seller for information regarding pick up and price. Book details and contact informatiion is available on the website'

EMAIL_HOST_USER = 'noreplybookorder@gmail.com'

EMAIL_HOST_PASSWORD = 'bookorder123'

EMAIL_PORT = 465
