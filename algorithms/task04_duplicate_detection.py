# Lab Task: Duplicate Detection in an Array
# Goal: Determine if any element appears more than once
# Approach: Compare each element with the elements that come after it (i + 1 to n)
# Time Complexity: O(n^2) - Brute force pairwise comparison

A = [14, 50, 55, 70, 56]
n = len(A)
has_duplicate = False

for i in range(n):
    for j in range(i + 1, n):
        if A[i] == A[j]:
            has_duplicate = True
            break
    if has_duplicate:
        break

if has_duplicate:
    print("TRUE")
else:
    print("FALSE")

# Practical Note:
# For large inputs, using a set or hash table achieves O(n) time:
# has_duplicate = len(A) != len(set(A))
