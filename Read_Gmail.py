import imaplib, email, os

user='innovaters3d@gmail.com'
password='sucodxwhspfoompx'
imap_url='imap.gmail.com'
attachment_dir= "C:/Users/stars/MyPythonScripts" #directory of attachments to be saved to


#reads raw HTML body of an email
def get_booty(msg):
    if msg.is_multipart():
        return get_booty(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

#download attachments and save to file. Input=byte data of email
def get_attachments(msg):
    for part in msg.walk():     #go through parts of message
        if part.get_content_maintype()=='multipart':    #if the maintype of the email is multitype (msg+attachement)    
            continue                                
        if part.get('Content-Disposition') is None:    
            continue
        #obtain filename from the part
        fileName=part.get_filename()
        
        #check if filename is boolean (if false then attachment isnt there)
        if bool(fileName):
            #joining attachment_dir (directory) with the fileName
            filePath= os.path.join(attachment_dir, fileName)
            #opening a file standard way as filehandle (wb=writing bytes)
            with open(filePath,'wb') as fh:
                fh.write(part.get_payload(decode=True)) #payload=attachent ,decodes=True decodes attachment whend downloaded
                

#searching the email fn input= key, value and connection
def search(key,value,con):
    result,data =con.search(None,key,'"{}"'.format(value))
    return data

#iterate through emails fetching them emails, returns msgs
def get_emails(result_bytes):
    msgs=[]
    for num in result_bytes[0].split():
        typ, data=con.fetch(num,'(RFC822)')
        msgs.append(data)
    return msgs


    
con=imaplib.IMAP4_SSL(imap_url)
con.login(user,password)
con.select('INBOX')

#set result and data to fetch from byte email #3 protocol=RFC822
result, data=con.fetch(b'1','(RFC822)')

#raw data part in byte form
raw=email.message_from_bytes(data[0][1])
#call get_attachment
get_attachments(raw)

#Call print the functions and pass raw byte data 
#print(get_booty(raw))
