a="hello world"
out=' '
for i in a:
    if a[i] in range(len(a)):
     if a[i] not in out a[i+1:]:
            out+=a[i]
print(out)
