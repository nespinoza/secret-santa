# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import shuffle, randint
import smtplib
import yaml
import json
import ssl


def email_meta_loader() -> dict:
	"""Utility function to load email parameters."""

	with open('_config.yml') as config:
		meta = yaml.load(config, Loader=yaml.FullLoader)

	return meta


def load_emails(emails_path : str) -> list:
	"""Utility function to load emails list."""

	with open(emails_path) as emails_file:
		emails = json.load(emails_file)

	return emails


def assign_partner(emails : list) -> list:
	"""Utility function to match partners from emails list."""

	n = len(emails)
	if n < 2:
		raise ValueError(f'List must have at least 2 emails, it has {n} elements')

	shuffle(emails)
	start = 0
	while start < n - 1:
		# Choose the cut for the cycle
		cut = randint(start + 2, n - 1) if start + 2 < n - 1 else n
		if cut == n - 1: cut = n
		# Assign the cycle
		for i in range(start, cut):
			emails[i]['assigned'] = emails[(i + 1) % cut]['name']
		# Reset the range
		start = cut

	return emails


def send_email(email : dict, user : dict) -> None:
	"""Utility function to send email to a specific user."""

	# Setup email configurations:
	message = MIMEMultipart('alternative')
	message['Subject'] = email['subject']
	message['From'] = email['email']
	message['To'] = user['email']

	# Load email body:
	with open(email['body']) as body:
		html = body.read()

	html = html.format(user['name'], user['assigned'])
	body = MIMEText(html, 'html')
	message.attach(body)

	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
		server.login(email['email'], email['password'])
		server.sendmail(
			email['email'], user['email'], message.as_string()
		)


if __name__ == "__main__":
	email = email_meta_loader()
	emails = load_emails(email['list'])
	assign_partner(emails)
	print(emails)
