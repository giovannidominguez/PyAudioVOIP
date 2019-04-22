
import socket
import pyaudio
import wave
import time
import sys

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(2), channels=1, rate=44100, output=True, frames_per_buffer=1024)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', int(sys.argv[1])))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024)

frames = []

print "Receiving\n"

while data != '':
    stream.write(data)
    data = conn.recv(1024)
    frames.append(data)

wf = wave.open("ServerRecording.wav", 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()

stream.stop_stream()
stream.close()
p.terminate()
conn.close()

print "Success! wav file of the recording saved\n"
