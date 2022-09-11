print(range(1,10))# range will not work alone it will work with for and known as generator. Gentrator returns object (itreative) 
def getcubes(limit=9):
    for i in range (1,limit+1):
        yield i**3 # yield maens storing it in the memeory


print('🎇'*20)

for val in getcubes():
    print(val)

print('✨'*20)
for val in getcubes(5):
    print(val)


print('🎆'*20)

def prime(start=2, stop=100):
    for num in range(start,stop):
        for i in range(start ,stop):
            if num % i==0:

                break   
        else:

            yield num


for p in prime(stop=100):
    print(p)