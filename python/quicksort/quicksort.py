from datetime import datetime
import random


def quicksort(a: list[int]):

    def swap(i, j):
       a[i], a[j] = a[j], a[i]

    def qsort_rec(low: int, high: int):
        if high - low < 1:
            return
        pivot, i, j = a[high], low, high - 1
        while i <= j:
            if a[i] > pivot:
                if a[j] <= pivot:
                    swap(i, j)
                j -= 1
            else:
                i += 1
        swap(i, high)
        qsort_rec(low, i - 1)
        qsort_rec(i + 1, high)

    qsort_rec(0, len(a) - 1)


def test_sort(a, b):
    print(f"testing {a} -> {b}")
    quicksort(a)
    assert a == b


if __name__ == "__main__":

    test_sort([], [])
    test_sort([4, 2, 8, 5, 6, 1, 4], [1, 2, 4, 4, 5, 6, 8])
    test_sort([1, 2, 3, 4], [1, 2, 3, 4])
    test_sort([-1, -2, -3, -4], [-4, -3, -2, -1])

    size = 1_000_000
    bigarray = [random.randint(-1000, 1000) for _ in range(size)]
    start = datetime.now()
    quicksort(bigarray)
    end = datetime.now()
    print(f"sorted array of size {size} in {end - start}")
