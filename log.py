import logging
import socket
import json
from datetime import datetime
s = socket.socket()
s.connect(('irc.chat.twitch.tv', 6667))
s.send(f"PASS oauth:\r\n".encode("utf-8"))
s.send(f"NICK \r\n".encode("utf-8"))
s.send(f"JOIN #\r\n".encode("utf-8"))
while True:
    message = ''
    r = s.recv(2048).decode('utf-8')
    if r.startswith('PING'):
        s.send("PONG\n".encode('utf-8'))
    elif len(r)>0:
        _1 = r.split(":")[2]
        _2 = r.split("!")[0].split(":")[1]
        if _1.startswith("Welcome, GLHF!") or _1.startswith("theyoshipvp.tmi.twitch.tv") or _1.startswith("tmi.twitch.tv"):
            pass
        elif len(_1)>0:
            message = _1
        if _2.startswith("tmi.twitch.tv"):
            pass
        elif len(_2)>0:
            username=_2
        now = datetime.now().strftime('%d-%m-%Y, %H:%M:%S')
        try:
            dicts = {"username":username, "message":message, "date":now}
            out_file = open("logs.json", "a+")
            json.dump(dicts, out_file, indent=6)
            out_file.write(",")
            out_file.close()
        except:
            pass
