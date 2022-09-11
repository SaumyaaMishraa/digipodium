n=int(input("enter="))
a=input('a=')
b=input("b=")
res,res2="",""
for i in range(len(a)):
    if a[i]!= b[i]:
        res+= a[i]
        res2+=b[i]
        for j in set (a):
            if j not in a:
                print(n-1)
                break
            else:
                print(len (set (res2)))