A = []

n = int(input("\nEnter the number of integers: "))
print("")

for p in range(n):
    q = int(input("Enter integer: "))
    A.append(q)

print("\nEntered Array: ")
print(A)

# -----------------------------------------------

for i in range(len(A)):
    # Minimum element in unsorted array
    min_i = i

    for j in range(i+1, len(A)):
        if A[min_i] > A[j]:
            min_i = j

    # Swap minimum element with first element
    A[i], A[min_i] = A[min_i], A[i]

# -----------------------------------------------

print("\nSorted Array: ")
print("[", end="")

for i in range(len(A)):
    print(A[i], end="")
    if(i<len(A)-1):
        print(", ", end="")

print("]")

'''
OUTPUT:

Enter the number of integers: 5

Enter integer: 43
Enter integer: 21
Enter integer: 25
Enter integer: 3
Enter integer: 16

Entered Array:
[43, 21, 25, 3, 16]

Sorted Array:
[3, 16, 21, 25, 43]
'''