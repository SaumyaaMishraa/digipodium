# create a listr of n numeric elements
# generate a list of only even numbers
# generate a list of only odd numbers
# generate a list of only > n from existing list,where n can be any value

x=[]
for i in range (5):
    val = int(input(f'enter value {i}:'))
    x.append(val)
print('list:',x)

y=[]
for i in x:
    if i %2 == 0:
        y.append(i)

print("odd no. :",y)


z=[]
for i in x:
    if i %2 !=0:
        z.append(i)

print("even no. :",z)


m5=[]
for i in x:
    if i>5:
        m5.append(i)
print ( 'no. greater then 5:', m5)


    