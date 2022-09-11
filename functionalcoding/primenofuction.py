a=0
def prime(x):
    if x>=2:
     for i in range (2,x):
        if not (x%i):
            return False
    else:
        return False
    return True

for m in range  (int(input('enter the the no. = '))):
    if prime(m):
        a +=1
        print (m) 
    print('we found a prime number')