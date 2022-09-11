# string validation

value=input("enter your name with desig. =")
if value.startswith('Mr.'):
    print('hello sir')
elif value.startswith('Ms.'):
    print('hello mam') 
elif value.startswith('Dr.'): 
   print('hello doc!')
elif value.startswith('Er.'):  
   print('hello you are welcome')
else :
    print('sorry !! not invited')