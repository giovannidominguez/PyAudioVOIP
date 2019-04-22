import sys
import socket
import pyaudio

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

p = pyaudio.PyAudio()

stream1 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
stream2 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

print("Listening...\n")

frames = []

for i in range(0, int(44100 / 1024 * int(sys.argv[3]))):
 data  = stream1.read(1024)
 frames.append(data)
 s.sendall(data)

print("Voice Chat Successful!\n")

stream1.stop_stream()
stream1.close()
p.terminate()
s.close()

print("Chat Closed\n")
