a = 5

a += 5
print("By Addition Assignment += :" , a) # 10

a -= 3
print("By Subtraction Assignment -= :" , a) # 7

print("=======================================")

b = 15

b *= 2
print("By Multiplication Assignment *= :" , b) # 30

b /= 4
print("By Division Assignment /= :" , b) # 7.5  (Returns quotient) (Always returns float value)

print("=======================================")

c = 25

c %= 3
print("By Modulus Assignment %= :" , c) # 1   (Returns reminder)

c = 20
c //= 6
print("By Floor Division Assignment //= :" , c) # 3   (Returns quotient)

c **= 4
print("By Exponentiation Assignment **= :" , c)  # 3*3*3*3 = 81

print("=======================================")

print("Below operators works on binary values")
d = 12
e = 5

d &= e
print("By Bitwise AND Assignment &= :" , d)  # 4

f = 12
g = 5
f ^= g
print("By Bitwise XOR Assignment ^= :" , f)  # 9

print("=======================================")

h = 12
i = 5
h >>= i
print("By Right Shift Assignment >>= :" , h) # 0

j = 12
k = 5
print("By Left Shift Assignment >>= :" , j) # 12




















