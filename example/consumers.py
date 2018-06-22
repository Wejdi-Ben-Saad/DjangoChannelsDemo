from channels import Group
import json

def ws_connect(message): 
    message.reply_channel.send({"accept": True}) 
    Group('chat').add(message.reply_channel)

def ws_receive(message):
    incomingData = json.loads(message.content["text"])     
    Group('chat').send({ "text": incomingData['user']+":"+incomingData['text']}) 


def ws_disconnect(message): 
    Group("chat").discard(message.reply_channel)    


