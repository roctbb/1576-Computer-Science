import wave, struct
import pyaudio

# открыть файл
file = wave.open("result.wav")
# узнать количество фреймов
n = file.getnframes()
# считываем из файла фреймы
data = file.readframes(n)

p = pyaudio.PyAudio()

sample_width = p.get_format_from_width(file.getsampwidth())
output_stream = p.open(format=sample_width,
                channels=file.getnchannels(),
                rate=file.getframerate(),
                output=True)
output_stream.write(data)
output_stream.close()