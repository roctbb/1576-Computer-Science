from PIL import Image

dog_image = Image.open("dog.jpg")
pixels = dog_image.load()

width = dog_image.width
height = dog_image.height

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        a = (r+g+b)//3
        r = a
        b = a
        g = a
        pixels[i, j] = (r, g, b)

dog_image.show()

