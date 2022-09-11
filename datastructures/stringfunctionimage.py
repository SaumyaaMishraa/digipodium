value=input("enter file name =")
if value.endswith('.png'):
    print('its a png file')
elif value.endswith('.jpg'):
    print('its a jpg file') 
elif value.endswith('.docx'): 
   print('its a doc file')
elif value.endswith('.py') or value.endswith('.pynb'):  
   print('its a python file')
else :
    print('unidentified file, destroy your computer')