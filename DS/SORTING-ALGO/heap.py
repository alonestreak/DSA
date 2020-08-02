def max_heapify(A,n,i):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
        #print(largest,l)
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
        #print(largest,r)
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,n, largest)
        

#no of leaf nodes = (floor of n/2 +1) to n



def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def build_max_heap(A):
    n = len(A)//2
    for i in range(n, -1,-1):
        max_heapify(A,n, i)

def heap_sort(A):
    n=len(A)
    build_max_heap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        max_heapify(A,i,0)

    return A




A=[33,35,42,10,7,8,14,19,48]
print(heap_sort(A))
