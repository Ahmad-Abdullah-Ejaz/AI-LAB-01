# Lab Task: Python Lists - Indexing, Slicing & Iteration

# List initialization
my_list = ["black", "white", "red", "green"]

print("my_list:", my_list)
print("Type:", type(my_list))
print("Length:", len(my_list))

print("-" * 30)

# Positive and negative indexing
# Index 0: first item, Index -1: last item, -3: 3rd from end
print("my_list[0]  (first):", my_list[0])
print("my_list[-3] (3rd from end):", my_list[-3])

print("-" * 30)

# List slicing [start:end] -> end index is excluded
print("Slice [0:2]:", my_list[0:2])  # items at index 0 and 1
print("Slice [1:2]:", my_list[1:2])  # item at index 1

print("-" * 30)

# Iterating through elements
print("Iterating through list:")
for item in my_list:
    print(" -", item)
