a=input('enter a string')
i = 1
count = 0
while i<len(a):
    if a[i] in 'aeiou':
        count+=1
    i+=1
print(count)                                                                                                                                                                       