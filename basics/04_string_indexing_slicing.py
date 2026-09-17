# Lab Task: Python Strings - Quotes, Indexing & Access

# 1. String literal formats and quote handling
# You can use single quotes inside double quotes and vice versa
str1 = "Hello PYTHON"
str2 = "Day's"
str3 = 'Days"s'

print("str1:", str1)
print("str2:", str2)
print("str3:", str3)

print("-" * 35)

# 2. String indexing (0-based from left, -1 from right)
text = "Python Hands-on-practice"
print("Full string:", text)

print("text[0]   :", text[0])    # 'P'
print("text[4]   :", text[4])    # 'o'
print("text[14]  :", text[14])   # 'p'
print("text[-15] :", text[-15])   # 'H'
print("text[-1]  :", text[-1])    # 'e' (last character)
