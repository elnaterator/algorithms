from datetime import datetime
import random

def quicksort(a: list[int]):
    """Sorts a list of integers in place using quicksort algorithm."""
    
    def swap(i, j):
        v = a[j]
        a[j] = a[i]
        a[i] = v
        
    # 5, 8, 7
    # i
    # j
    # pivot = 5
    
    def qsort_rec(low: int, high: int):
        if high - low < 1:
            return
        pivot, i, j = a[high], low, high-1
        while i <= j:
            if a[i] > pivot:
                if a[j] <= pivot:
                    swap(i, j)
                j -= 1
            else:
                i += 1
        swap(i, high)
        qsort_rec(low, i-1)
        qsort_rec(i+1, high)
            
    qsort_rec(0, len(a) - 1)
    

if __name__ == "__main__":
    #a = [random.randint(-1000, 1000) for _ in range(1000000)]
    a = [4, 2, 8, 5, 6, 1, 4]
    start = datetime.now()
    quicksort(a)
    print(datetime.now() - start)
    print(a)
    

    