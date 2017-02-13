def selection_sort(array):
    sorted_array = []
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                new_min = array[i]
            if array[i+1] < new_min:
                new_min = array[i+1]
        sorted_array.append(new_min)
    return sorted_array

if __name__ == "__main__":
    import random
    # array = [random.randint(-1000,1000) for _ in range(100)]
    array = [4,5,8,10,16,1,-1000,14,6,-5,-420]
    print "\nUnsorted Array: {}\n".format(array)
    sorted_array = selection_sort(array)
    print "\nSorted Array: {}\n".format(sorted_array)
