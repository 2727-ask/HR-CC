inputs = input().split()
row = int(inputs[0])
col = int(inputs[1])
a = ".|."
for x in range(1,row,2):
    print((str(a)*x).center(col,'-'))
print('WELCOME'.center(col,'-'))
for y in range(row-2,-1,-2):
    print((str(a)*y).center(col,'-'))
