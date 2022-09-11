
a=input("enter whatever you want= ")
if a.isnumeric():
    print("only no.= ",a.isnumeric())
elif a.isalnum():
    print( 'alpha numeric=',a.isalnum())
elif a.isalpha():
    print('only alphabets', a.isalpha())
elif a.isspace():
    print('only spaces', a.isspace())
else:
    print('done')

