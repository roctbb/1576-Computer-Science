from speechkit import text_to_record, record_to_text
import wave, struct, pyaudio
import random
import vk


def play_file(name):
    file = wave.open(name)
    n = file.getnframes()
    data = file.readframes(n)
    play(data, framerate=file.getframerate())

def play(data, framerate=44100):
    p = pyaudio.PyAudio()
    output_stream = p.open(format=pyaudio.paInt16,
                           channels=1,
                           rate=framerate,
                           output=True)
    output_stream.write(data)
    output_stream.close()


def record(seconds, framerate=16000):
    p = pyaudio.PyAudio()
    chunk = 1024
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

name = input()

service_token = "2feef6c285d89838e0f23489f6a0ebb93d4ae9660e5544b25b9cc72dd8b5067ac1fa72ccd56b5164b3ba1"
session = vk.Session(access_token=service_token)
api = vk.API(session)
result = api.wall.search(domain="kinopoisk", count=100, query=name, v=5.65)
print(result)
if result["count"]!=0:
    for i in range(10):
        text = random.choice(result["items"])["text"]
        print(text)
        file = text_to_record(text)
        play_file(file)
