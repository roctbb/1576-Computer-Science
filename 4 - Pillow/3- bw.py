from PIL import Image

dog_image = Image.open("dog.jpg")
pixels = dog_image.load()

width = dog_image.width
height = dog_image.height

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        r = 255 - r
        g = 255 - g
        b = 255 - b

        if (r + g + b)//3 > 127:
            r = 255
            g = 255
            b = 255
        else:
            r = 0
            g = 0
            b = 0
        r = min(r + 150, 255)
        pixels[i, j] = (r, g, b)

dog_image.show()

