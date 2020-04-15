# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(cur_index)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # TO-DO: find next smallest element

        # (hint, can do in 3 loc) 

        # TO-DO: swap

    return arr

arr = list(range(1,11))
import random
random.shuffle(arr)
print(selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps_occured = True
    while swaps_occured: 
        swaps_occured = False

        for i in range(len(arr) - 1): 
            print(arr)

            if arr[i] > arr[i+1]: 
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occured = True

    return arr

arr = list(range(1,11))
import random
random.shuffle(arr)
print(bubble_sort(arr))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr