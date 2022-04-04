from twilio.rest import Client

accountSID = 'ACe8e7555a9072dc5e8568df7490d10495'

authToken = '064bcaff6e392e81842522c5e02ba9ff'

client = (Client(accountSID,authToken))

TwilioNumber = '+18509403540'

mycell = '+19368278305'

textmessage = client.messages.create(to=mycell,from_=TwilioNumber,body="Hello World")

print(textmessage.status)

#how to make a phone call
call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml", to=mycell, from_= TwilioNumber)