#acessing the string characters
from __future__ import print_function


str= 'digipodium'
print('str =', str)

# acessing 1st charater
print( 'string looks likes =  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 ' ,'digipodium',' 0 1 2 3 4 5 6 7 8 0 ') 
print('str[0]', str[0])

print ("str[-3]", str[-3])

#slicing  of a string
slice1=str[4 : 7]
print(slice1)

slice2=str[-6:-1]
print(slice2)


#both ways are same
slice3=str[0:len(str)]
print(slice1)

slice4=str[:5]
print(slice1)

slice4=str[0:7]
print(slice1)

name= 'vijay deenanath chauhan'
fname= name[:5]
lmane= name[-7:]
mname= name[6:-8]
print(name, fname,mname)

#reverse
rev_name= name[::-1]
rev_mname= name[6:-8][::-1]
print(rev_name,rev_mname)

#every even index 
even_name =name [::2]
#every odd index 
odd_name =name [1::2]

print(even_name,odd_name)


