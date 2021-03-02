count = int(input())
list = []
for x in range(0,count):
    a=input().replace(" ","")
    list.append(a)
print(len(set(list)))
