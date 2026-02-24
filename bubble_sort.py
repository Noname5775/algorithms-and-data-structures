from typing import List

def bubble_sort_optimized(a: List[int]) -> List[int]:
    n = len(a)
    arr = a.copy()
    for i in range(n):
        swapped = False
        # Проходим до n - 1 - i, так как последние i элементы уже на месте
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если за прохода не было обменов — массив отсортирован
        if not swapped:
            break
    return arr
print(bubble_sort_optimized([5,1,4,2,8]))
