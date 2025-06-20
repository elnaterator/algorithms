from datetime import datetime
import random


def bubblesort(a: list[int]):

    def swap(i, j):
        v = a[j]
        a[j] = a[i]
        a[i] = v

    for last_index in range(len(a) - 1, 0, -1):
        for i in range(0, last_index):
            if a[i] > a[i + 1]:
                swap(i, i + 1)


def test_sort(a, b):
    print(f"testing {a} -> {b}")
    bubblesort(a)
    assert a == b


if __name__ == "__main__":

    test_sort([], [])
    test_sort([4, 2, 8, 5, 6, 1, 4], [1, 2, 4, 4, 5, 6, 8])
    test_sort([1, 2, 3, 4], [1, 2, 3, 4])
    test_sort([-1, -2, -3, -4], [-4, -3, -2, -1])

    size = 1_000_000
    bigarray = [random.randint(-1000, 1000) for _ in range(size)]
    start = datetime.now()
    bubblesort(bigarray)
    end = datetime.now()
    print(f"sorted array of size {size} in {end - start}")
