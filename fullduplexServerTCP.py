import socket
import pyaudio


CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000

#HOST/PORT of server *HARDCODED* to be changed
HOST = '169.231.83.171'
PORT = 40001

def openStream(format, channels, rate, type, frames, p):
    if type == 'input':
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    elif type == 'output':
        stream = p.open(format=FORMAT,
                         channels=CHANNELS,
                         rate=RATE,
                         output=True,
                         frames_per_buffer=CHUNK)
    return stream



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
connection, client_addr = s.accept()
print 'Connected by', client_addr

p = pyaudio.PyAudio()


mystream = p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  output=True,
                  frames_per_buffer=CHUNK)

mystream2 = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   frames_per_buffer=CHUNK)



while 1: #try statements for recieving and sending audio data respectively
    try:
        data = connection.recv(1024)
        mystream.write(data)
    except KeyboardInterrupt:
        print ("error 1")
        break

    try:
        data2  = mystream2.read(CHUNK)
        connection.sendall(data2)
    except KeyboardInterrupt:
        print ("error 2")
        break


#close the stream and pyaudio object


mystream.stop_stream()
mystream.close()
p.terminate()
connection.close()
