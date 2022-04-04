import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch("Outlook.Application")
outlook_ns = outlook.GetNamespace("MAPI")


myfolder = outlook_ns.Folders['collin_covington1@baylor.edu'].Folders['Inbox']

messages = myfolder.Items


for message in messages:
    messagecount =+ 1


accountSID = 'ACe8e7555a9072dc5e8568df7490d10495'

authToken = '064bcaff6e392e81842522c5e02ba9ff'

client = (Client(accountSID,authToken))

TwilioNumber = '+18509403540'

mycell = '+19368278305'

textmessage = client.messages.create(to=mycell,from_=TwilioNumber,body=str(messagecount))

print(textmessage.status)