"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if array:
        pivot = array[len(array)-1]
        pivot_orig = pivot
        pivot_index = len(array)-1
        #pivot_flag = 0
        cmp_index = 0
        stop_index = 0
        start_index = 0
        while pivot_index != stop_index:
            if pivot < array[cmp_index]:
                if pivot_index-1 == cmp_index:
                    temp = array[pivot_index - 1]
                    array[pivot_index - 1] = pivot
                    array[pivot_index] = temp
                    pivot_index -= 1
                    #print (array)
                else:
                    temp = array[pivot_index - 1]
                    array[pivot_index - 1] = pivot
                    array[pivot_index] = array[cmp_index]
                    array[cmp_index] = temp
                    pivot_index -= 1
                    #print (array)
            else:
                cmp_index += 1

            if pivot_index == 0:
                pivot_index = len(array)-1
                cmp_index = stop_index
                start_index = stop_index
                pivot = array[pivot_index]

            if cmp_index == pivot_index and pivot_index != start_index:
                if pivot == pivot_orig:
                    stop_index = pivot_index + 1
                pivot_index -= 1
                cmp_index = start_index
                pivot = array[pivot_index]


        return array


    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))