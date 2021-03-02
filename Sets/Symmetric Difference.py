na = int(input())
a = set(input().split())
nb = int(input())
b = set(input().split())
diff = list(map(int ,a.difference(b)))+list(map(int,b.difference(a)))
ans= (sorted(diff))
for x in ans:
    print(x)