def selection_sort(array):
    

if __name__ == "__main__":
    import random
    array = [random.randint(-1000,1000) for _ in range(100)]
    print "\nUnsorted Array: {}\n".format(array)
    sorted_array = selection_sort(array)
    print "\nSorted Array: {}\n".format(sorted_array)
