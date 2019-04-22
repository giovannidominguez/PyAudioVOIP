#!/usr/bin/python

import socket
import pyaudio
import wave

CHUNK_LISTEN = 64
CHUNK_SEND = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 64000
WIDTH = 2
SECONDS = 15

p1 = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()
stream = p1.open(format=p1.get_format_from_width(WIDTH),
                 channels=CHANNELS,
                 rate=RATE,
                 output=True,
                 frames_per_buffer=CHUNK_LISTEN)

stream2 = p2.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK_SEND)

HOST = '169.231.152.37'
PORT = 55000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = (HOST, PORT)
print server_addr
s.bind(server_addr)

while 1:
    # data, address = s.recvfrom(8192)
    # stream.write(data)

    # receiving data
    try:
        data, address = s.recvfrom(8192)
        stream.write(data)
        print address
    except KeyboardInterrupt:
        break
    except:
        pass

    # sending data
    try:
        data2 = stream2.read(CHUNK_SEND, exception_on_overflow=False)
        s.sendto(data2, address)
    except KeyboardInterrupt:
        break
    except:
        pass
