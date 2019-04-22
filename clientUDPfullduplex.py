#!/usr/bin/python

import socket
import pyaudio
import wave

CHUNK_SEND = 1024
CHUNK_LISTEN = 64
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 64000
WIDTH = 2
SECONDS = 15

HOST = '169.231.152.37'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (HOST,PORT)
print ('Connected to: ', server_addr)
p = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SEND)
stream2 = p2.open(format=p.get_format_from_width(WIDTH), channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK_LISTEN)
print ("now listening!")
while 1:
    #send data
    try:
        data = stream.read(CHUNK_SEND, exception_on_overflow=False)
        s.sendto(data,server_addr)
    except:
        print ("pass 1")
    try:
        data2, addr = s.recvfrom(8192)
        stream2.write(data2)
    except:
         print ("pass 2")

#stream.stop_stream()
#stream.close()
#stream2.stop_stream()
#stream2.close()
#p.terminate()
#p2.terminate()
