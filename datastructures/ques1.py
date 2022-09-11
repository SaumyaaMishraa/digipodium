from string import ascii_lowercase
#swap to count all the charater in a string
# dispaly output like
# a-3
# b-9
# ...
#z-0

word= [ 'you can do it' , 'you work it out' , 'god will help you', "bee buzz"]
quote=' '.join (word)
print(quote)
for char in ascii_lowercase:
    print (f'{char}- {quote.count(char)}')
 

#other way is
count_a = quote.count('a')
print(' a =', count_a)
count_b = quote.count('b')
print(' b =', count_b)
count_z = quote.count('z')
print(' z =', count_z)