import pyaudio
import struct

p = pyaudio.PyAudio()

chunk = 1024
framerate = 44100


def record(seconds):
    input_stream = p.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=framerate,
                          input=True,
                          frames_per_buffer=chunk)
    data = b""
    for i in range(int(seconds * framerate / chunk)):
        data = data + input_stream.read(chunk)
    input_stream.close()
    return data


def play(data):
    output_stream = p.open(format=pyaudio.paInt16,
                           channels=1,
                           rate=framerate,
                           output=True)
    output_stream.write(data)
    output_stream.close()

def make_high(data):
    frames = struct.unpack("@{}h".format(len(data)//2), data)
    frames = frames[::2]
    return struct.pack("@{}h".format(len(frames)), *frames)


for i in range(3):
    data = record(3)
    data = make_high(data)
    play(data)
