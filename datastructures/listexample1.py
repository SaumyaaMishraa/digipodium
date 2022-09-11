x=[]
for i in range (10):
    val = input(f'enter value {i+1}:')
    x.append(val)

print('the list')
x.sort()
for val in x:
    print(val,end="")
    print(''.join(x))

