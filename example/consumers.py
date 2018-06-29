from channels import Group
import json
from channels.auth import channel_session_user, channel_session_user_from_http

###### WS CHAT ######
@channel_session_user_from_http
def ws_connect(message): 
    message.reply_channel.send({"accept": True}) 
    Group('chat').add(message.reply_channel)
    Group('chat').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })

@channel_session_user
def ws_receive(message):
    incomingData = json.loads(message.content["text"])     
    Group('chat').send({ "text": message.user.username+":"+incomingData['text']}) 

@channel_session_user
def ws_disconnect(message):
    Group('chat').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('chat').discard(message.reply_channel)

###### WS USER LIST ######
@channel_session_user_from_http
def ws_connect_user_list(message): 
    message.reply_channel.send({"accept": True}) 
    Group('chat').add(message.reply_channel)    

@channel_session_user
def ws_receive_user_list(message):
    incomingData = json.loads(message.content["text"])     
    Group('chat').send({ "text": message.user.username+":"+incomingData['text']}) 

@channel_session_user
def ws_disconnect_user_list(message):    
    Group('chat').discard(message.reply_channel)


