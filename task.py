from helper import read
data = read('pride_n_prejudice.txt')

#1.display the top 100 words that occur in the file
#cleaning
#all wors list
#loop count each word and put ans in dict
#sort the dict with value

def clean(data):
    from string import punctuation
    for p in punctuation:
        data.replace(p,'')
    return data

def word_count(words): 
 for w in set(words):
    wordcount={}
    wordcount[w]=words.count(w)

words= clean(data).lower().split()
wordcount={}
wc= word_count(words)
wc=sorted(wc.items(),lambda d: d[-1])
print(wc[:100])
print(wordcount)

print(len(words),'unique=',len(set(words)))
print(set(words))