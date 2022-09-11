#nested dict
from pprint import pprint
employees= {
    'chandu':{
    'name':'chandu sharma',
    'salary':15000,
    'desgination':'foreman'
  }, 
   'rohit':{
   'name':'rohit kumar sharma',
   'salary':19999,
   'desgination':'asssitant2',
    'manager':'ravi prakash'
  },
 
  'bhanu':{
  'name':'bhanu prakash singh',
  'salary':18999,
 'desgination':'asssitant3',
 }
} 

pprint(employees)

print('desigination',employees['chandu'],['desgination'])

for key,data in employees.items():
    print(key,'💖')
    for k,v in data.items():
        print(k,v,'👀')
    print('--'*10)