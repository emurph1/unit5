#Emily Murphy
#2017-11-27
#quickSort.py -quick sort algorithm

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def mySort(A, lo, hi):
    if lo <hi:
        p = partition(A,lo,hi)
        mySort(A,lo,p-1)
        mySort(A,p+1,hi)
    return A
        
def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1
    for j in range(lo,hi-1):
        if A[j] < pivot:
            A[j], pivot = pivot, A[j]
    if A[hi] < A[i+1]:
        A[hi], A[i+1] = '', A[hi]
    return A

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers, 0, len(numbers)-1)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
