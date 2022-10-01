from PIL import Image,ImageFilter,ImageEnhance,ImageDraw,ImageFont
im=Image.open("flower.jpg")
im2= Image.open(r'C:\Users\saumy\Documents\digipodium\flower.jpg')

print(im)
print(im2)

im.rotate(45).show()
im2.rotate(90).show()
print('redolution',im.size)
print('height',im.height)
print('mode',im.mode)
#im.resize((100,100)).show()
#im.resize((2000,2000)).show()
#im.resize((im.width*5, im.height*5)).save('flower_x5.jpg')
#im.filter(ImageFilter.EMBOSS).show()
#im.filter(ImageFilter.CONTOUR).show()
#im.filter(ImageFilter.BLUR).show()
#im.filter(ImageFilter.SHARPEN).show()
#im.filter(ImageFilter.SMOOTH).show()
#im.filter(ImageFilter.MinFilter(5)).show()
#im.filter(ImageFilter.MedianFilter).show()


#eim= ImageEnhance.color(im)
#for i in range (-10,11,2):
#    eim.enhance(i).show()

imc= im.copy()
im2_s= im2.resize(200,160)
imc.paste(im2,(200,200))
imc.show()