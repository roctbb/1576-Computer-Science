from PIL import Image

# импортируем модуль для запросов в интернет
import requests


# это адрес сервиса для распознавания эмоций
url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

# словарь с двумя элементами - типом данных и ключом доступа
header = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": "4f2ad86f11724c5287d94a2efb2731c6"
}

# открываем файл с картинкой в бинарном режиме (rb) и читаем из него все
image = open('people.jpg', 'rb').read()

# отправляем запрос в microsoft прикладывая к нему словарь с заголовками и саму картинку
# ответ попадает в result
result = requests.post(url, headers=header, data=image)


# парсим json и на выходе получаем словарь с лицами
faces = result.json()

print(faces)

big_image = Image.open("people.jpg")


# в цикле выводим координаты каждого лица
for face in faces:
    print('--- '*10)
    print("x - ", face['faceRectangle']['left'])
    print("y - ", face['faceRectangle']['top'])
    print("w - ", face['faceRectangle']['width'])
    print("h - ", face['faceRectangle']['height'])

    x = face['faceRectangle']['left']
    y = face['faceRectangle']['top']
    width = face['faceRectangle']['width']
    height = face['faceRectangle']['height']

    emotions = face['scores']
    print(emotions)

    max_emotion = 'anger'
    max_value = 0

    for emotion in emotions:
        if emotions[emotion] > max_value:
            max_value = emotions[emotion]
            max_emotion = emotion

    print(max_emotion, " - ", max_value)

    if max_emotion == "neutral":
        smile = Image.open(max_emotion+".png").convert("RGBA")
    else:
        smile = Image.open("face.png")

    smile = smile.resize((width, height))
    big_image.paste(smile, (x,y), smile)

big_image.show()
