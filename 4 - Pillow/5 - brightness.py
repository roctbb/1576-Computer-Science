from PIL import Image

dog_image = Image.open("dog.jpg")
pixels = dog_image.load()

width = dog_image.width
height = dog_image.height

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        r = min(r + 150, 255)
        b = min(b + 150, 255)
        g = min(g + 150, 255)
        pixels[i, j] = (r, g, b)

logo_image = Image.open('logo.png')
logo_image = logo_image.resize((600, int((600/logo_image.width) * logo_image.height)))

dog_image.paste(logo_image, (0,0), logo_image)

dog_image.show()

