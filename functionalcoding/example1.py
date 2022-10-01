def area():
 l= int(input('enter the length '))
 b= int(input('enter the breadth '))
 area=l*b
 return area

print('area=>',area())
ans=area()
print('area=>',ans)

ans= area()+ area() - area()
print('total area =',ans)