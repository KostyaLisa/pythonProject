def bubble_sort(A):
    itretions = 0
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            itretions += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A, itretions

A= [2,5,9,1,8,6]
print(bubble_sort(A))

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubbel_sort_un_an_op(A):
    iteration = 0

    for i in A:
        for j in range(len(A)-1):
            iteration+=1
            if A[j]>A[j+1]:
                swap(A,j,j+1)
    return A,iteration

A= [2,5,9,1,8,6]
print(bubbel_sort_un_an_op(A))