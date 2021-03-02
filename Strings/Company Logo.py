from collections import Counter
s = sorted(input())
arr=Counter(s).most_common(3)
for x in arr:
    print(x[0],x[1])