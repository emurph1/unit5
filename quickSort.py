#Emily Murphy
#2017-11-27
#quickSort.py -

"""algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p - 1 )
        quicksort(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo - 1    
    for j := lo to hi - 1 do
        if A[j] < pivot then
            i := i + 1
            swap A[i] with A[j]
    if A[hi] < A[i + 1] then
        swap A[i + 1] with"""
        
def quickSort(A, lo, hi):
    if lo <hi:
        p = 
        
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j = lo to hi - 1:
        if A[j] < pivot:
            A[j], pivot = pivot, A[j]
    if A[hi] < A[i+1]:
        A[hi], A[i+1] = '', A[hi]