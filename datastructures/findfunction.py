#find and index are same (similar)

msg= 'this is a place to find the answer related to coding.'

print("place:",msg.find('place'))
print('placle:',msg.find('placle'))

val=msg.find('answer')
if val== -1:
    print('word not found')
else:
    print (f"word found at {val} index")

print('is:', msg.find("is"))
print('is:', msg.index("is"))

print('is:', msg.index("is",3))

print('to',msg.find('to'))
print('to',msg.rfind('to')) #sreach from reverse