import socket
import pyaudio

CHUNK = 64
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 64000
WIDTH = 2

OST = '169.231.152.37'
PORT = 40000

HOST = None
PORT = None
s = None

def setUpConnection(add):
   setUpSocket(add)

def setUpSocket(address):
   global s
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.bind(address)

def configureHostAndPort():
   global HOST, PORT
   HOST = raw_input("Enter Local IP:")
   PORT = int(raw_input("Enter Port # :"))
   print HOST
   print PORT


p = pyaudio.PyAudio()

def openStream(format, channels, rate, frames):
   stream = p.open(format=FORMAT,
               channels=CHANNELS,
               rate=RATE,
               output=True,
               frames_per_buffer=CHUNK)
   return stream

def main():
   configureHostAndPort()
   server_addr = (HOST,PORT)
   setUpConnection(server_addr)
   mystream = openStream(FORMAT, CHANNELS, RATE, CHUNK)
   while 1:
       data, address = s.recvfrom(8192)
       mystream.write(data)
main()
