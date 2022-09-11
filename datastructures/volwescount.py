msg= input('ENTER THE SENTENCE:')
for vowel in 'aeiou':
  print(vowel, msg.lower().count(vowel))