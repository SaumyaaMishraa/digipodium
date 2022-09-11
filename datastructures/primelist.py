prime=[]
for i in range (2,100):
    for m in range (2,i):
      if i % m ==0:
          break
    else:
        prime.append(i)

for p in prime:
    print(p,end=",")

