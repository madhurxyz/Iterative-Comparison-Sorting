def bubble_sort(array):
    is_sorted = True
    while is_sorted:
        is_sorted = False
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = True
    print array
    return array

if __name__ == "__main__":
    import random
    array = [random.randint(1,100) for _ in range(1000)]
    bubble_sort(array)
