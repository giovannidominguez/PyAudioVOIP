#!/usr/bin/python

import socket
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 64000

HOST = '169.231.152.37'
PORT = 40000

HOST = None
PORT = None
s = None
#establish socket connections and configure port functions
def setUpConnection():
    setUpSocket()

def setUpSocket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def configureHostAndPort():
    global HOST, PORT
    HOST = raw_input("Enter the host IP:")
    PORT = int(raw_input("Enter host's port #:"))
    print HOST
    print PORT





p = pyaudio.PyAudio()

def openStream(format, channels, rate, frames):
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    return stream
#main runs HOST/PORT Functions and opens stream to send data
def main():
    configureHostAndPort()
    setUpConnection()
    server_addr = (HOST, PORT)
    mystream = openStream(FORMAT, CHANNELS, RATE, CHUNK)

    while 1:
        data  = mystream.read(CHUNK)
        s.sendto(data,server_addr)

main()
