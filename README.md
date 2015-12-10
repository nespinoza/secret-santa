# secret-santa

This code assumes you were assigned to take care of the pairing of a Secret Santa at 
your company/institution, and you are too lazy to:

    1. Pair the people.
    2. Send the e-mails to let people know who got who.

Of course, this code can easily be modified to send automatic notifications to you 
or someone every week (e.g., running the code as a cronjob), e-mail yourself when you want 
to know when that piece of code that is running on a screen is actually finished or, simply, 
to spam people about that awesome event you are planning and you want them to attend (yes; 
personalized e-mails are better at this job than just sending an entire e-mail chain to all 
your invitees).

Author: Néstor Espinoza (nsespino@uc.cl)

DEPENDENCIES
------------

This code makes use of:

    + The python email library.
    + The python numpy library.
    + The python smptp library.

All of them are free to download and use.

USAGE
------------
Create a list of the names + e-mails as in the example file attached to this code (list_of_emails.txt). 
Then, create the e-mail in any format you like but keeping in mind that [Parameter1] and [Parameter2] 
will be changed in the actual e-mail by the name of the person you are sending the e-mail to and 
the person that was assigned to the receiver of the e-mail respectively (both parameters taken from the 
list_of_emails.txt file).

In order to send the e-mails, just modify the parameters of the ho-ho-ho.py file (yes, it is intended to 
sound like Santa's laugh) adding your e-mail, password, subject of the e-mail and your name as you 
want it to be seen next to your e-mail (you can put "REAL SANTA" if you want). Finally, just run 
the ho-ho-ho.py code and you are good to go.
