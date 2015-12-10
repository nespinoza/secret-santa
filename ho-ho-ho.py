#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib,random,sys
from numpy import copy,loadtxt
from email.mime.text import MIMEText
import smtplib
import email.mime.multipart as M

def SwapString(TEXT,search_string,input_string):
 n=0
 m=len(search_string)
 for k in range(len(TEXT)):
    if(TEXT[k:k+m]==search_string):
      n=k
 if(n==0):
   'String '+search_string+' not found. Returning the same input text...'
   return TEXT
 return TEXT[0:n]+input_string+TEXT[n+m:len(TEXT)]

################## Parameters ########################
email_to_send = 'email.txt'
emails_list = 'list_of_emails.txt'

the_email_subject = '[Secret Santa] You must give a present to...'
sender_name = 'Your name as you want it to appear on the e-mail'
your_email = 'your_email@gmail.com'
password = 'your_password'
######################################################

# Open the file that contains the e-mail list:
name,email = loadtxt(emails_list,dtype='string',unpack=True,usecols=(0,1))
name_a,email_a = copy(name),copy(email)

# Create a pairing of each e-mail until all of them are paired with different 
# persons. In the long-run, this method is faster ;-):
match=True
while(match):
 random.shuffle(name_a)
 match=False
 for i in range(len(name_a)):
     if(name[i]==name_a[i]):
       match=True

# E-mail sender...
fromaddr = your_email
# Credentials...
username = your_email
# Connection with the server...
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
msg = M.MIMEMultipart()
# E-mail sending...
for i in range(len(name)):
 s=name[i]
 # We fix the names, which can be introduced as name-lastname:
 for j in range(len(s)):
   if(s[j]=='-'):
     s=s[0:j]+' '+s[j+1:len(s)]
     thename=s[0:j]
     j=0
 name[i]=s
 s=name_a[i]
 for j in range(len(s)):
   if(s[j]=='-'):
     s=s[0:j]+' '+s[j+1:len(s)]
     j=0
 name_a[i]=s
 # Fixed! Now we open the text as an e-mail message:
 fmsg = open(email_to_send,'rb')
 TEXT = fmsg.read()
 fmsg.close()
 # We search and swap some strings...
 S = SwapString(TEXT,'[Parameter1]',thename)
 S = SwapString(S,'[Parameter2]',name_a[i])

 # Prepare the e-mail...
 toaddrs = email[i]
 msg=MIMEText(S)
 de = sender_name+' <'+fromaddr+'>'
 to = name[i]+' <'+email[i]+'>'
 msg['Subject'] = the_email_subject
 msg['Reply-to'] = fromaddr
 msg.add_header('to',to)
 msg.add_header('from',de)
 server.sendmail(fromaddr,toaddrs,msg.as_string())
 print 'E-mail sent to '+to+'!'
server.quit()
