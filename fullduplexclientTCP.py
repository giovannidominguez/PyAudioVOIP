import socket
import pyaudio
import wave


CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 20000

#default HOST/PORT
HOST = '169.231.152.37'
PORT = 40002

HOST = None
PORT = None
s = None
#HOST AND PORT CONFIGURATIONS
def configureHostAndPort():
    global HOST, PORT
    HOST = raw_input("Enter the host IP:")
    PORT = int(raw_input("Enter host's port #:"))
    print HOST
    print PORT
#    print ("Attempting connection with " + HOST + " on port " + PORT)

def setUpSocket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def setUpConnection():
    setUpSocket()
    s.connect((HOST, PORT))

p = pyaudio.PyAudio()



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




#Main runs HOST/PORT functions and opens two streams to send/recieve audio data


def main():
    # for sending data
    configureHostAndPort()
    setUpConnection()
    stream = openStream(FORMAT,
                        CHANNELS,
                        RATE,
                        'input',
                        CHUNK,
                        p)

    # for receiving data
    stream2 = openStream(FORMAT,
                         CHANNELS,
                         RATE,
                         'output',
                         CHUNK,
                         p)

    print("Listening...")

    while True:

     try:		# sending data
         data  = stream.read(CHUNK, exception_on_overflow = False)
         s.sendall(data)
     except KeyboardInterrupt:
         print ("error1")
         break

     try:       	# receiving data
         data2 = s.recv(1024)
         stream2.write(data2)
     except KeyboardInterrupt:
        print ("error2")
        break


    print("Done Listening!")



#close stream and pyaudio object

    stream.stop_stream()
    stream.close()
    p.terminate()
    s.close()

    print("Stream is closed")

main()
