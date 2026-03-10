import random
import time
import matplotlib.pyplot as plt


# пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)

    # проходим по массиву
    for i in range(n):

        for j in range(0, n - i - 1):

            # если элементы стоят неправильно — меняем
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# сортировка слиянием
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# создаём случайный массив
def generate_array(size):

    arr = []

    for i in range(size):
        number = random.randint(0, 10000)
        arr.append(number)

    return arr


# измеряем время работы
def measure_time(sort_function, arr):

    start = time.time()

    sort_function(arr.copy())

    end = time.time()

    return end - start


sizes = [1000, 5000, 10000, 50000]

bubble_times = []
merge_times = []


for size in sizes:

    array = generate_array(size)

    bubble_time = measure_time(bubble_sort, array)
    merge_time = measure_time(merge_sort, array)

    bubble_times.append(bubble_time)
    merge_times.append(merge_time)

    print("Размер массива:", size)
    print("Bubble Sort:", bubble_time)
    print("Merge Sort:", merge_time)
    print()


plt.plot(sizes, bubble_times, label="Bubble Sort")
plt.plot(sizes, merge_times, label="Merge Sort")

plt.xlabel("Размер массива")
plt.ylabel("Время (секунды)")
plt.title("Сравнение алгоритмов сортировки")

plt.legend()

plt.show()
