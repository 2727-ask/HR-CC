from collections import Counter
no = 4
list = []
for x in range(no):
    s = input()
    list.append(s)
c = Counter(list)
v = ((c.values()))
print(len(c))
for x in v:
    print(x,end=" ")
