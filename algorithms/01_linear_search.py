# Lab Task: Linear Search on a List
# Goal: Check if a target value exists in a single list
# Time Complexity: O(n) - worst case scans entire list

target = 78
numbers = [12, 34, 56, 78, 99]

found = False

# Linear search logic
for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        break  # stop early once match is found

if found:
    print("TRUE")
else:
    print("FALSE")

# Note: In standard Python, we can also simply write:
# if target in numbers:
#     print("TRUE")
