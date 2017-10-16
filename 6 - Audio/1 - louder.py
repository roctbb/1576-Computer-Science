import wave, struct

file = wave.open("task.wav")

n = file.getnframes()

data = file.readframes(n)

frames = struct.unpack("@{}h".format(n), data)

frames = list(frames)

for i in range(len(frames)):
    frames[i] = frames[i] * 10

frames = frames[::-2]

loud_data = struct.pack("@{}h".format(n//2), *frames)

loud_file = wave.open("result.wav", "wb")
loud_file.setparams(file.getparams())
loud_file.writeframes(loud_data)
loud_file.close()