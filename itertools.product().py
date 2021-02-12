from itertools import product
data = []
a1 = (input()).split()
b1 = (input()).split()
data.append(a1)
data.append(b1)

print (list(product(*data)))


