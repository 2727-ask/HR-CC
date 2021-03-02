ignores = input().split()
Happiness = 0
Arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
for x in Arr:
    if x in A:
        Happiness =Happiness+1
    elif x in B:
        Happiness = Happiness-1
    else:
        pass
print(Happiness)



