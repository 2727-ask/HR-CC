str = "abcdcee"
list = []
dic = {}
for x in str:
    if x in dic:
        print(x)
        dic[x]=dic[x]+1
        break
    else:
        dic[x]=1
print(dic)

