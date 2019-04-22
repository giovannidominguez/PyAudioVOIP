import pyaudio
import wave

format_type = pyaudio.paInt16
num_channels = 2
sample_rate = 44100
seconds = 5
chunk = 1024
name = "newfile.wav"

my_audio = pyaudio.PyAudio()
 
# start Recording
stream = my_audio.open(format=format_type, channels=num_channels, rate=sample_rate, input=True, frames_per_buffer=chunk)
print ("Listening...")
frames = []
 
for i in range(0, int(sample_rate/ chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)
print ("finished recording! newfile.wav created!")

stream.stop_stream()
stream.close()
my_audio.terminate()
 
waveFile = wave.open(name, 'wb')
waveFile.setnchannels(num_channels)
waveFile.setsampwidth(my_audio.get_sample_size(format_type))
waveFile.setframerate(sample_rate)
waveFile.writeframes(b''.join(frames))
waveFile.close()
