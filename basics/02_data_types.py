# Lab Task: Python Data Types & type() Inspection
# Exploring Integers, Floats, Complex Numbers, and Booleans

# 1. Dynamic User Input & Casting
num = int(input("Enter a number: "))
print("num:", num)
print("Type:", type(num))

print("-" * 35)

# 2. Integers (both positive and negative)
a = 1452
print("a:", a, "| Type:", type(a))

b = -4587
print("b:", b, "| Type:", type(b))

print("-" * 35)

# 3. Floating-point numbers (standard & scientific notation)
# 2.12e-10 means 2.12 * 10^(-10)
c = 2.12e-10
print("c:", c, "| Type:", type(c))

# 5E220 means 5 * 10^220
k = 5E220
print("k:", k, "| Type:", type(k))

print("-" * 35)

# 4. Complex Numbers (real + imag*j)
# Can be created via complex(real, imag) or literal notation (1 + 2j)
x = complex(1, 2)
print("x:", x, "| Type:", type(x))

z = 1 + 2j
print("z:", z, "| Type:", type(z))

print("-" * 35)

# 5. Booleans (True / False)
flag_t = True
flag_f = False
print("flag_t:", flag_t, "| Type:", type(flag_t))
print("flag_f:", flag_f, "| Type:", type(flag_f))
