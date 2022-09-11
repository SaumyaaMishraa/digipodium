name= ['ravi singh','raj singh','suraj thakur','mohan yadav','ravi mishra', 'suraj mishra','rohit singh','vijay kumar','vatsala mishra','saumya mishra']
name_singh= list(filter(lambda n:n.startswith('r'),name))
name_singh1= list(filter(lambda n:n.endswith('singh'),name))
print(name_singh1)
print(name_singh)
