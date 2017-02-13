def selection_sort(source):
    for i in range(len(array)):
        minimum = min(array[i:])
        min_index = array[i:].index(minimum)
        array[i + min_index], array[i] = array[i], array[i + min_index]
    return array

if __name__ == "__main__":
    import random
    array = [random.randint(-1000,1000) for _ in range(100)]
    print "\nUnsorted Array: {}\n".format(array)
    sorted_array = selection_sort(array)
    print "\nSorted Array: {}\n".format(sorted_array)
