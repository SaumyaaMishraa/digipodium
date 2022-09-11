fib=[]
for i in range (20):
    val = input(f'enter value {i+1}:')
    fib.append(val[-1]+val[-2])
    print(fib)
    for val in fib:
     print(val,end=" ")


    