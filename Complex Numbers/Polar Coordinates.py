import math,cmath
txt = input()
ctxt = complex(txt)
x = (ctxt.real)
y = (ctxt.imag)



r = math.sqrt(int(x)**2 + int(y)**2)
w = cmath.phase(ctxt)
print(r)
print(w)

