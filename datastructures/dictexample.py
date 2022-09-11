#create a contact dict, where the user can search for a person
#name and if the name exist , it dispaly the phone number
#else , the number of that person
#alsothe user can chooose to the list all person and number

from pprint import pprint
contacts= {
    'SAUMYA':{
    'name':'Saumya Mishra',
    'phone_no': 83186813542
  }, 
   'SHRUTI':{
   'name':'Shruti Mishra',
   'phone_no':99341884242
  },
 
  'ARPIT':{
   'name':'Arpit Shukla',
   'phone_no':9233434222
  },
  'RIYA':{
   'name':'riya rao',
   'phone_no':'not available'
 } 

}

for key,data in contacts.items():
    print(key,'💖')
    for k,v in data.items():
        print(k,v)
    print('--'*15)

print(contacts)
def search(name, phone_no):
    for i in range (len(contacts)):
        if contacts[i]==phone_no :
         return True
    return False

name=['Saumya Mishra', 'phone_no', 'SHRUTI', 'phone_no', 'ARPIT', 'RIYA']
phone_no='not available'

while True:
    print('# option')
    print('1= search person')
    print('2= view all')
    print('3= exist')
    ans= input('select your desire option :')
    if ans=='1':
        name= input('enter persons name')
        if name in contacts:
            print(f'{name} => {contacts[name]}')
        else:
         print(f'Not found: would you like to put the {name} no.')
        number= input('enter the phone no. for the person =>')
        contacts[name] = number
        pprint('details added')
    elif ans=='2':
     for name, number in contacts.items():
        print('details added',contacts)
    elif ans=='3':
     print('BYE')
    break
else:
    print('wrong input')
