
"""
time complexity=o(n^2)

useful for smaller datasets

"""

def selection_sort(A):
    for i in range(0,len(A)-1):
        min_val=i
        for j in range(i+1,len(A)):
            if A[j]<A[min_val]:
                min_val=j


        if min_val!=i:
            A[i],A[min_val]=A[min_val],A[i]

    return A

print(selection_sort([5,6,7,1,0,90,-5]))
