
from channels.routing import route
from example.consumers import ws_connect, ws_disconnect, ws_receive, ws_connect_user_list, ws_disconnect_user_list, ws_receive_user_list 

channel_routing = [
    route('websocket.connect', ws_connect, path=r'^/$'),
    route('websocket.disconnect', ws_disconnect, path=r'^/$'),
    route("websocket.receive", ws_receive, path=r'^/$'),

    route('websocket.connect', ws_connect_user_list, path=r'^/user_list/'),
    route('websocket.disconnect', ws_disconnect_user_list, path=r'^/user_list/'),
    route("websocket.receive", ws_receive_user_list, path=r'^/user_list/'),
]


