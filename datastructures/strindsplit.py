a1= input("enter a sentence: ")
word = a1.split()
print(word, len(word),'words found')


word = a1.split(",")
print(word, len(word),'words found')


word = a1.split("is")
print(word, len(word),'words found')

word = a1.split()[-3:]
print(word, len(word),'words found')
