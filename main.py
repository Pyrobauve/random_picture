import random
from PIL import Image, ImageFilter, ImageDraw

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)
img = Image.new('RGB', (500, 500), color = (R,G,B)) #create background color, dimension = 500*500
draw = ImageDraw.Draw(img)

for x in range(0, random.randint(40,100)):
#-- Set random number in variable--
    choice = random.randint(1,2)

    x1 = random.randint(0,500)
    y1 = random.randint(0,500)
    x2 = random.randint(0,500)
    y2 = random.randint(0,500)
    x3 = random.randint(0,500)
    y3 = random.randint(0,500)

    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
#----------------------------------

    if choice == 1: #Generate polygon with random coordonates and random colors

       draw.polygon([(x1,y1), (x2, y2), (x3,y3)], fill = (R,G,B))

    elif choice == 2: #Generate circle with random coordonates and random colors

       draw.ellipse((x1, y1, x2, y2), fill = (R,G,B))
       draw.point((x3, y3))

blurImage = img.filter(ImageFilter.GaussianBlur(3)) #Add blur filter

blurImage.save('picture.png') #Save picture
