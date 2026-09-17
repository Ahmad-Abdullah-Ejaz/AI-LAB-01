# Lab Task: Search Across Two Separate Lists
# Goal: Search for an element sequentially in two lists (list1 then list2)
# Time Complexity: O(n + m) where n and m are lengths of num1 and num2

target = 78
num1 = [12, 34, 56, 78, 99]
num2 = [10, 44, 51, 21, 67]

found = False

# Search in the first list
for i in range(len(num1)):
    if num1[i] == target:
        found = True
        break

# If not found in num1, search in num2
if not found:
    for i in range(len(num2)):
        if num2[i] == target:
            found = True
            break

if found:
    print("TRUE")
else:
    print("FALSE")
