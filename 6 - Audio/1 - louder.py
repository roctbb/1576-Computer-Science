import wave, struct

# открыть файл
file = wave.open("task.wav")
# узнать количество фреймов
n = file.getnframes()
# считываем из файла фреймы
data = file.readframes(n)
# распаковываем строку из байт
frames = struct.unpack("@{}h".format(n), data)
# получили список с фреймами
frames = list(frames)

# делаем громче
for i in range(len(frames)):
    frames[i] = frames[i] * 10
# разворачиваем и увеличиваем частоту
frames = frames[::-2]

# обратно в байт-строку
loud_data = struct.pack("@{}h".format(n//2), *frames)

# сохраняем в новый файл
loud_file = wave.open("result.wav", "wb")
loud_file.setparams(file.getparams())
loud_file.writeframes(loud_data)
loud_file.close()