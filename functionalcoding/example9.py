#variable arguments =args
#keywords arguments= kwargs

def total(*values):
    t=0
    for i in values:
        if isinstance(i,(int,float)):
            t+=i
    return t

o= total(1,2,3,4)
print(o)
o= total(1,2,321,4,345,345,2,3,4,5,687,1,2,3,4,5)
print(o)
o= total(1,2,3,4,5,6,7,8,9)
print(o)
o= total(1,2,'3',4,5,6,7,8) #'3'will be ignored and only int values are totaled
print(o)
