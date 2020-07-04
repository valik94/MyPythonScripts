#Reading Email inbox #Searching through email
from imapclient import IMAPClient

server = IMAPClient('imap.outlook.com', use_uid=True)
server.login('starshiy@live.ca', 'Valik1994')

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])

messages = server.search(['FROM', 'noreply@steampowered.com']) #(['FROM','EMAIL YOU WANT TO SEARCH FROM'])
print("%d messages from our best friend" % len(messages))

for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
	envelope = data[b'ENVELOPE']
	print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))

server.logout()
