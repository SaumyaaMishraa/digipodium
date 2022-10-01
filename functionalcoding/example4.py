def word_counter(s):
    words =s.split()
    return len(words)

def area (l,b):
    return l*b

def circumference(r):
    return 2* 3.14* r

print(word_counter('this is a example'))
print(word_counter("Welcome to the code of python"))
print(word_counter(' screenshort se kuch nai hoga'))
print(word_counter('rules and covention likh lo!!!!'))

#call area and circumfernce
#1. direct
print(area(10,10))

#2.user input
a=int(input('enter length=') ) 
b=int(input('enter breadth=') )
out= area(a,b)
print('area=',out)

#3.short user input
out= area(int(input('enter length=') ) ,int(input('enter breadth=') ))
print('area=',out)

