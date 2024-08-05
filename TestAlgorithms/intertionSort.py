def insertion_sort (A):
    for j in range(1,len(A)):
        key = A[j]
        i=j -1
        while i >= 0 and A[i]>key:
            A[j+1]= A[i]
            i-=1
        A[i+1]=key
    return A

A= [2,5,9,1,8,6]
print(insertion_sort(A))