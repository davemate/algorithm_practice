data = []

def quick_sort(array_to_sort):
    if(len(array_to_sort) == 0):
        return []
    #pick a pivot
    pivot = array_to_sort.pop(0)

    #Iterate through items and partition into two seperate arrays
    larger_array = []
    smaller_array = []
    for element in array_to_sort:
        if element >= pivot:
            larger_array.append(element)
        else:
            smaller_array.append(element)
    return quick_sort(smaller_array) + [pivot] + quick_sort(larger_array)


print(quick_sort(data))