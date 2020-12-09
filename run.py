# -*- coding: utf-8 -*-

from mail_utils import email_meta_loader
from mail_utils import assign_partner
from mail_utils import load_emails
from mail_utils import send_email

if __name__ == "__main__":
        email = email_meta_loader()
        emails = load_emails(email['list'])
        assign_partner(emails)

        for user in emails:
                print('[INFO] Sending email to {}'.format(user['email']))
                send_email(email, user)
