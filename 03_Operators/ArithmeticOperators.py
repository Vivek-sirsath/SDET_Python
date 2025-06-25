a = 10  # int
b = 5 # int

print("Addition -", a+b) # 15
print("Subtraction -", a-b) # 5
print("Multiplication -", a*b) # 50
print("Division -", a/b) # 2.0   ---> float
print("Floor Division -", a//b) # 2  ---> int --> Round up to the nearest whole number.
print("Modulo Division -", a%b) # 0  ---> reminder
print("Exponent / Power -", a**b) # 100000  ---> a^b ---> 10^5

print("=========================================================")

x = 10.0  # float
y = 5  # int

print("Division -", x/y) # 2.0   ---> float
print("Floor Division -", x//y) # 2.0  ---> int
print("Modulo Division -", x%y) # 0.0  ---> reminder
print("Exponent / Power -", x**y) # 100000.0  ---> a^b ---> 10^5

print("=========================================================")

j = 55.2  # float
k = 12.3  # float
print("Division -", j/k) # 4.48780487804878   ---> float
print("Floor Division -", j//k) # 4.0  ---> float
print("Modulo Division -", j%k) # 6.0  ---> reminder
print("Exponent / Power -", j**k)  # 2.665941750535956e+21

print("=========================================================")

m = 45
n = 21
print("Division -", m/n)  # 2.142857142857143  (Quotient)
print("Floor Division -", m//n)   # 2  (Quotient Round Up) (int because both are int, trim fraction part)
print("Modulo Division -", m%n)   # 3  (Reminder)

print("=========================================================")

p = 137
q = 23
print("Division -", p/q)  # 5.956521739130435  (Quotient)
print("Floor Division -", p//q)   # 5  (Quotient Round Up) (int because both are int, trim fraction part)
print("Modulo Division -", p%q)   # 22 (Reminder)