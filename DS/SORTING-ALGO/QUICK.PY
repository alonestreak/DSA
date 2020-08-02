from random import randint

def quick_sort(a):
    if len(a)<=1:
        return a

    smaller,equal,larger=[],[],[]
    pivot=a[randint(0,len(a)-1)]
    for x in a:
        if x<pivot:
            smaller.append(x)
        elif x==pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort(smaller)+ equal+ quick_sort(larger)

#print(quick_sort([2,6,4,3,-12,990,45]))



def quick_sort_inplace(a,low=0,high=None):
    if high==None:
        high=len(a)-1
    if low<high:
        p_idx=partition(a,low,high)
        quick_sort_inplace(a,low,p_idx-1)
        quick_sort_inplace(a,p_idx+1,high)
    return a
    
    
    
def partition(a,low,high):
    i=low-1
    pivot=a[high]
    for j in range(low,high):
        if a[j]<=pivot:
            i+=1
            a[i],a[j]=a[j],a[i]
            print(a[i],a[j])

    a[i+1],a[high]=a[high],a[i+1]
    print("out")
    print(a[i+1],a[high])
    return i+1

a=[2,6,49,56,66,3,46,-12,990,45]
print(len(a))
quick_sort_inplace(a)
print(a)
