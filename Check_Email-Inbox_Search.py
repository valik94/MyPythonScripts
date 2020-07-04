import imapclient, datetime, pyzmail

conn=imapclient.IMAPClient('imap.gmail.com',ssl=True)
conn.login('innovaters3d@gmail.com','sucodxwhspfoompx')
conn.select_folder('inbox',readonly=True)
UIDs = conn.search(['SINCE', datetime.date(2020, 6, 13)]) #IMAP Search Keys table16-3 Examples: 'BEFORE date' ; 'ON date' ; 'SINCE date' ;    'SUBJECT string', 'BODY string' , 'TEXT string'
print(UIDs)
#prints = Unique IDs --Ex. [1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459]
rawMessage= conn.fetch([1448],['BODY[]','FLAGS'])   # passing exact email ID, body and flags
message= pyzmail.PyzMessage.factory(rawMessage[1448][b'BODY[]']) #just function calls and passing email ID and bytes of body
#call get_subject fn to print subject
message.get_subject()                       #Ex. 'The Power Of Saying Less | Tim Denning in The Startup'
#call get address to print address from
message.get_addresses('from')               #Ex.[('Medium Daily Digest', 'noreply@medium.com')]
message.get_addresses('to')                 #Ex. [('innovaters3d@gmail.com', 'innovaters3d@gmail.com')]
#check if emails have text emails or HTML emails
message.text_part   #if not none then its no text email
message.html_part   #if not None then it has HTML components
message.text_part.get_payload().decode('UTF-8') #read the email contents (decode to UTF-8)
#Checking draft or spam folder (finding folders)
conn.list_folders()

#to modify/delete folders
conn.select_folder('inbox', readonly=False)
conn.delete_messages([1448]) #1448 is the email id you delete, or pass all UIDs to delete all selected
#for more documentation go to:
#imapclient.readthedocs.org/en/latest/
#magiksys.net/pyzmail/
#automate the boring stuff chapter16
