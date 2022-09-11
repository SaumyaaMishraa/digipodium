
#patterns

#example1 5pyramid 
print('For the pyramid pattern insert value of rows')
rows= int(input("no. of rows = "))
for i in range(rows):
 for j in range(i+1):
  print('*', end="")
 print()

# example2 inverted pyramid
print('For the pyramid pattern insert value of rows')
row= int(input("no. of rows = "))
for m in range(row):
  for n in range(m,row):
    print('*', end="")
  print()