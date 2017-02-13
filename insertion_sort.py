def insertion_sort(array):
    first = array[0]
    new_array = []
    new_array.append(first)
    for i in range(1, len(array)):
        if array[i]>new_array[i]:
            new_array.append(array[i])


if __name__ == "__main__":
    import random
    array = [random.randint(-1000,1000) for _ in range(100)]
    insertion_sort(array)
