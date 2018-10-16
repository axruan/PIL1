from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

for i in range(0, 512):
    for j in range(0, 512):
        image.putpixel((i,j), (j, i, i))

image.save("demo.png", "PNG")
