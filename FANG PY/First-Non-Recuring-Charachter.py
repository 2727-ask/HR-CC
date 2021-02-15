str = "AABCCDE"
dic = {}
for x in str:
    if x in dic:
        dic[x] = dic[x] + 1
    else:
        dic[x] = 1



print(dic)
for x in dic:
    if dic[x]==1:
        print(x)
        break
