fruits =['cherry', 'guvava','apple', 'banana']
dry_fruits=['almond','cashew']
fruits.sort()
print(fruits)

fruits.extend(dry_fruits)
print(fruits)

fruits.append(dry_fruits)
print(fruits)

fruits.insert(1,'orange')
print(fruits)

slice1=fruits[2:4]
print(slice1)
