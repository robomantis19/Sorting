# STRETCH: implement Linear Search				
def linear_search(arr, target):
  found = False
  if found == True: 
    for i in arr: 
      arr[i] == target
      return 1
  else: 
  # TO-DO: add missing code

    return -1   # not found


arr = list(range(1,11))
import random
random.shuffle(arr)
print(linear_search(arr, 15))

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  while low < high: 
    mid = (low + high) // 2 
    print('high', high)
    print('mid', mid)
    if arr[mid] == target or arr[high] == target:
      
      print('arr', arr[mid])
      print('target', target)
      return 1
    elif target < mid: 
      high = target
    else: 
      low = mid + 1
      
  return -1 # not found

arr = [-1, 1, 2, 3, 4, 5, 6]
print(binary_search(arr, 7))

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

  if arr == 0: 
    return -1
  low = 0 
  high = len(arr) - 1

  if(low < high):
    return binary_search_recursive(arr[low], target, (low+high)/2, high)

  # array empty
  # TO-DO: add missing if/else statements, recursive calls

arr = list(range(1,11))
import random
random.shuffle(arr)
print(binary_search_recursive(arr, 10, 1, 11))
