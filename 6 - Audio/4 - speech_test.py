from speechkit import text_to_record, record_to_text
import wave, struct, pyaudio

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

text = record_to_text(record(4))
file = text_to_record(text)
play_file(file)