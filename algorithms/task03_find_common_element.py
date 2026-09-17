# Lab Task: Check for Common Element Between Two Lists
# Goal: Check if there is any matching element between list A and list B
# Note on Bug Fix: original code compared A[i] == B[i] (positional match),
# while nested loops are intended for finding any common element (A[i] == B[j]).

A = [80, 14, 86, 78, 79]
B = [90, 44, 50, 78, 66]

n = len(A)
found = False

# Compare each element of A with every element of B
for i in range(n):
    for j in range(len(B)):
        if A[i] == B[j]:  # checking common element
            found = True
            break
    if found:
        break

if found:
    print("TRUE")
else:
    print("FALSE")

# Concept Note:
# - Brute-force approach: O(n * m)
# - Pythonic / optimized approach: set(A) & set(B) runs in O(n + m)
