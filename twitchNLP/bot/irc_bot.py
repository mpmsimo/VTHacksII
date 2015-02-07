"""
irc_bot.py - Connects to an IRC and logs chat using twisted library.
msimo - 2/6/15 - VTHacksII
Python 2.7.6
Modified version of ircLogBot provided by TwistedMatrix
"""

import socket
import string

HOST="irc.twitch.tv"
PORT=6667
NICK="darkiee"
IDENT="darkiee"
REALNAME="darkiee"
CHANNEL="#manvsgame"
PASSWORD="oauth:h9loaxtbpmt712zzrr6rzfsnt2bns6"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("PASS %s\r\n" % PASSWORD)
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s\r\n" % CHANNEL)

print("Connected to {}".format(CHANNEL))

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        if len(line) > 3:
            print line
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])