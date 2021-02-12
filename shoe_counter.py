from collections import Counter
dataAmount = int(input())


money = 0
myList = input().split()
data= (Counter(myList).items())
data_set=[]
for x in data:
    data_set.append(list(x))
cust = int(input())

for y in range(0,cust):
    value = input().split()


    for z in range(len(data_set)):
        if(value[0] in  data_set[z]):
            if int(data_set[z][1])>0:
                data_set[z][1] = int(data_set[z][1])-1
                money = money + int(value[1])
print(money)


