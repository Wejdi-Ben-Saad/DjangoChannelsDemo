from channels import Group
import json
from channels.auth import channel_session_user, channel_session_user_from_http


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


