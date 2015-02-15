"""
irc_bot.py - Connects to an IRC and logs chat using twisted library.
msimo - 2/6/15 - VTHacksII
Python 2.7.6
Modified version of ircLogBot provided by TwistedMatrix
"""

import socket, string, time, os

directory = (os.path.abspath(os.pardir)+"/data/chat_transcript/")
chat_dump = "chat_transcript_{}.txt"

hostname = "irc.twitch.tv"
port = 6667
nick = "darkiee"
ident = "darkiee"
realname = "darkiee"
#channel = "#sodapoppin"
#channel = "#wingsofdeath"
channel = "#phantoml0rd"
#oauth key has been changed since
password = "oauth:redacted"
readbuffer = ""

s = socket.socket()
s.connect((hostname, port))
s.send("PASS %s\r\n" % password)
s.send("NICK %s\r\n" % nick)
s.send("USER %s %s bla :%s\r\n" % (ident, hostname, realname))
s.send("JOIN %s\r\n" % channel)

print("Connected to {}".format(channel))

while 1:
    readbuffer = readbuffer + s.recv(1024)
    irc_chat = string.split(readbuffer, "\n")
    readbuffer = irc_chat.pop()

    chat_transcript_filename = (chat_dump.format(time.strftime("%Y%m%d-%H%M")))
    for line in irc_chat:
        line = string.rstrip(line)
        line = string.split(line)
        if len(line) > 3:
            line = line[3:]
            line = (" ".join(line).lower())
            f = open(directory+chat_transcript_filename, 'a+')
            f.write(line[1:]+"\n")
            print(line[1:])
