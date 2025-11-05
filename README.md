# secret-santa

This code assumes you were assigned to take care of the pairing of a Secret Santa at your company/institution, and you are too lazy to:

> 1. Pair the people.
> 2. Send the e-mails to let people know who got who.

Of course, this code can easily be modified to send automatic notifications to you or someone every week (e.g., running the code as a cronjob), e-mail yourself when you want to know when that piece of code that is running on a screen is actually finished or, simply, to spam people about that awesome event you are planning and you want them to attend (yes; personalized e-mails are better at this job than just sending an entire e-mail chain to all your invitees). 

Currently, the code works for google accounts only. Before using the code, you'll have to  activate the 'Less secure apps' from your gmail account or you'll get an SMTP Authentication  Error. I usually deactivate it when using the code, then activate it back again. You can do  this from here: https://www.google.com/settings/security/lesssecureapps.

## Changelog
- November, 2025. Updated code via Jules to make it compatible with latest `email` syntax.

## Dependencies

This code makes use of the following Python's libraries:

- `email`
- `random`
- `smtplib`
- `yaml`
- `json`
- `ssl`

All of them are already included in Python.


## How to use it

1. Modify the HTML code of the email body in the [email.txt](https://github.com/RodolfoFerro/secret-santa/blob/master/email.txt) file.
2. Modify the [_config.yml](https://github.com/RodolfoFerro/secret-santa/blob/master/_config.yml) file to add your Gmail credentials (mail/password):
```yaml
# Configuration file
body: email.txt
list: emails.json
subject: "[Future Lab] Tu amigo secreto es..."
sender: "Equipo Future Lab"
email: XXXXXXXXX@gmail.com
password: XXXXXXXXX
```
3. Modify the [emails.json](https://github.com/RodolfoFerro/secret-santa/blob/master/emails.json) file to add the people that will be assigned. The format of this JSON file must be as follows:
```txt
[
   ...
   {
      "name": "Person N",
      "email": "email_N@domain.com"
   },
   {
      "name": "Person N+1",
      "email": "email_N+1@domain.com"
   },
   ...
]
```
4. Finally, just run the main script:
```bash
$ python run.py
```


## License

This software contains a MIT License.

**Copyright (c) 2020 Nestor Espinoza**, with contributions from Rodolfo Ferro & Ivan Gonzalez
