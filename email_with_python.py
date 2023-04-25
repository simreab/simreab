import smtplib, getpass, imaplib, email

#send email
smtp_obj = smtplib.SMTP('smtp.gmail.com')
smtp_obj.ehlo()
smtp_obj.starttls()

email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')
smtp_obj.login(email, password)

from_address = email
to_address = email
subject = input('enter the subject line: ')
message = input('enter the body message: ')
msg = 'Subject: ' + subject + '\n' + message

smtp_obj.sendmail(from_address, to_address, msg)

smtp_obj.quite()


#receive email
M = imaplib.IMAP_SSL('imap.gmail.com')
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')
M.login(email, password)
M.list()
M.select('inbox')
typ, data = M.search(None, 'SUBJECT "NEW TEST PYTHON"')

email_id = data[0]
result, email_data = M.fetch(email,id, '(RFC822)')

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

from part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode= True)
        print(body)
