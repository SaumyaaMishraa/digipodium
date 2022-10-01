from PIL import Image,ImageDraw,ImageFont
im=Image.open("flower.jpg")
im2= Image.open(r'C:\Users\saumy\Documents\digipodium\flower.jpg')

font =ImageFont.truetype(r'C:\Users\saumy\Documents')
imd=ImageDraw.Draw(im)

imd.text ((100,100), 'flower', fill=(0,225,100),font=font)
im.show()