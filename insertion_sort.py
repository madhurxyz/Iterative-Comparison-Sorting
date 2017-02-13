def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and array[j-1] > item:
            array[j] = array[j-1]
            j = j - 1
        array[j] = item
    return array


if __name__ == "__main__":
    import random
    array = [random.randint(-1000,1000) for _ in range(100)]
    print "\nUnsorted Array: {}\n".format(array)
    sorted_array = insertion_sort(array)
    print "\nSorted Array: {}\n".format(sorted_array)
