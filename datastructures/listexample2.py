import statistics as stats

a=[]
for i in range (10):
    val = int(input(f'enter value {i}:'))
    a.append(val)

print('the list ')
a.sort()
for val in a:
    print(val,end=" ")

print("maximum value",max(a))
print("minimum value",min(a))
print("total of value",sum(a))
print("average of value",stats.mean(a))
print("median of value",stats.median(a))
print("mode value",stats.mode(a))

