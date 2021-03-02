bno = "101001"
flag = 0
c =0
o = 0
for x in bno:
    if x == "1":
        flag = 1
    else:
        flag = 0
        c = c+1
    print(flag)
print("c is",c)
