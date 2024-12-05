from imagNumber import ImagNumber

a = ImagNumber(-1,2)
b = ImagNumber(3,-4)

c = a + b
d = a - b

print(f"A: {a.asString()}")
print(f"B: {b.asString()}")
print(f"First: {c.real} + {c.imag}i")
print(f"Second: {d.real} + {d.imag}i")