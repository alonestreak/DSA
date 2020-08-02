"""
assume array has two parts
1] lest most part which have all sorted items
2] rest part os the arrsy which is unsorted

we will assume first element is sorted which will be always in first part
now we will take one element from item next to(on right side) of the array and instert into the appropriate part in the sorted array(this is done using inner while loop)

Time complexity=
best case(i.e when list is already sorted)= o(n)
average case=o(n^2)
worst case (sorted in opposite order) = o(n^2)


"""

def insertion_sort(A):
    for i in range(1,len(A)):#for loop to iterate over the list of unsorted items
        curNum=A[i]
        #print(curNum)
        while curNum <A[i-1] and i>0: # swap the elements until current element is in the correct position
            A[i],A[i-1]=A[i-1],A[i]
            i=i-1
    return A

c=[5,1,3,7,0,6]
ans=insertion_sort(c)
print(ans)
