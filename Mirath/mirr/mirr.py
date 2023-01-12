
l=[4,3,5,5,7]
print(len(l))
print(l[-1])
print(l[::-1])
if 5 in l:
    print('yes')
else:
    print('no')
print(l.count(5))
new = l[0:-1]
new.sort()
print(new)
