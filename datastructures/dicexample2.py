movies= {
    'm1':'Sholay',
    'm2':'Shrek',
    'm3':'Thor:love and thunder'

}
print(movies)
print(movies.keys())
print(movies.values())



#travesrsing a dictionary -> style1 -> gives only keys
print('style1')
for name in movies:
  print(name)

  #travesrsing a dictionary -> style2 -> gives only keys
print('style2')
for key in movies:
  print(movies[key])

 #travesrsing a dictionary -> style3 -> gives only keys
print('style3')
for key in movies:
  print(key,movies[key])

   #travesrsing a dictionary -> style4 -> gives only keys
print('style4')
for k,v in movies.items():
  print(k,v)

