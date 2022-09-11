x=[]
for i in range (10):
    val = int(input(f'enter value {i}:'))
    x.append(val)

x1=[]
x2=[]
for i in x:
    sqr=i**2
    x1.append(sqr)

print('no. of x list',x)
print('sqr of those no.',x1)

for i in x:
    cube=i**3
    x2.append(cube)
print('cube of those no.',x2)
