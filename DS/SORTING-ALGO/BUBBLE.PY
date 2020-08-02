"""
time complexity=o(n^2)
"""

def bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A
print(bubble([2,5,3,9,-12,-500,345,4]))
