import arrays
import random
from time import perf_counter

# Phase 1: Data Generation and Initial sorting using insertion sort

def generate_sorted_data(size):   # this is for an array of smaller size
    '''
    This function generates an array of given size using random integers between 1 and 100, and sorts the array using insertion sort
    size: int
    '''
    my_array = arrays.Array(size)   # creates an array of given size
    for i in range(len(my_array)):
        a = random.randint(1,100)   
        my_array[i] = a             # assigning each index in the array to a random integer between 1 and 100  
    for i in range(1,len(my_array)):
        key = my_array[i]           # assigning the element to be sorted in the iteration as key
        prev_i = i-1
        while prev_i>=0 and my_array[prev_i] > key:  # comparing all the elements in the unsorted part
            my_array[prev_i+1] = my_array[prev_i]
            prev_i = prev_i - 1
        my_array[prev_i+1] = key    # setting the element after the previous as the key
    return my_array

# Phase 2: Implementing binary search on sorted data
def binary_search(sorted_array, target):
    '''
    This function permits to perform binary search to find a target within a sorted array from the previously defined function in Phase 1
    and returns the index of the target when it finds it, or returns None if not found.
    sorted_array: array(list)
    target: int
    '''
    start = 0
    end = len(sorted_array) - 1   # initializations of start and end as index 0 and len - 1
    while end >= start:           # base case, as long as end is greater than start
        mid = (start + end) // 2  

        if target == sorted_array[mid]:
            return mid            
        elif target > sorted_array[mid]:
            start = mid + 1       # if target is bigger than mid, we move to the right of array, so start point is on the right of mid
        else:
            end = mid - 1         # if target is smaller than mid, we move to the left of array, so end point is on the left of mid
    return None

# Phase 3: Recursive merge sort for larger data
def generate_sorted_data(size): #larger dataset
    '''
    This function performs the same as the function from Phase 1, but this one generates an array with 1000 elements and sorts it.
    size: int
    '''
    my_array = arrays.Array(size)
    my_array = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)] # using comprehension list to make array with 990 elements
    for i in range(1,len(my_array)):
        key = my_array[i]
        prev_i = i-1
        while prev_i>=0 and my_array[prev_i] > key:
            my_array[prev_i+1] = my_array[prev_i]
            prev_i = prev_i - 1
        my_array[prev_i+1] = key
    return my_array
# print(generate_sorted_data(size=1000))

def merge_sec(array, start, mid, end):
    '''
    Helper function to merge two sorted half-arrays into one single sorted array
    array: array(list)
    start: int
    mid: int
    end: int   
    '''
    leftsize = mid - start + 1
    rightsize = end - mid       # finding the two sizes of the half-arrays

    leftpart = [0] * leftsize
    rightpart = [0] * rightsize  # creating temp arrays for both half-arrays

    for i in range(leftsize):
        leftpart[i] = array[start + i]  # copy data from first half into first temp
    for j in range(rightsize):
        rightpart[j] = array[mid + 1 + j]  # copy data from second half into second temp

    i = j = 0 
    k = start   # initialization for left and right half-array

    while i < leftsize and j < rightsize:  # merging both half-array into single 
        if leftpart[i] <= rightpart[j]:  # comparing element from left and right array
            array[k] = leftpart[i]
            i += 1
        else:
            array[k] = rightpart[j]
            j += 1
        k += 1
        
    while i < leftsize:
        array[k] = leftpart[i]    # copying rest of the elements from left
        i += 1
        k += 1

    while j < rightsize:
        array[k] = rightpart[j]   # copying rest of the elements from right
        j += 1
        k += 1

def merge_sort(array, start, end):
    '''
    This function uses recursive function algorithm and sorts the left anf right array and merges into single array.
    array: array(list)
    start: int
    end: int
    '''
    if start < end:  # base case, if start lesser than end 
       mid = (start + end) // 2
       merge_sort(array, start, mid)
       merge_sort(array, mid + 1, end)  # recursively sorting first and second half
       
       merge_sec(array, start, mid, end)  # merging the 2 half-array

def merge_sorted_data():
    '''
    This function uses the two previously defined functions and performs merge sort on the given array
    '''
    data = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90] + [random.randint(1, 100) for _ in range((990))]
    # data = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90]
    merge_sort(data, 0, len(data) - 1)  # calling merge sort with array "data" as parameter
    return data

def linear_search(sorted_array, target):
    '''
    This function performs linear search on a sorted array to find a given target
    sorted_array: array(list)
    target: int
    '''
    for i in range(len(sorted_array)):  # iterating thought the array
        if target == sorted_array[i]:   # checking if given target is equal to the element at index "i"
            return True
    return False

sorted_array = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90]
target = 72

# Phase 4: Search Performance Comparison
def search_perf_compare(sorted_array, target):
    '''
    This function compares the search times between linear search and binary search using the per_counter() function from time module
    sorted_array: array(list)
    target: int
    '''
    linear_start = perf_counter()
    linear_search(sorted_array, target)
    linear_end = perf_counter()
    linear_time = linear_end - linear_start  # difference in time before and after linear search

    binary_start = perf_counter()
    binary_search(sorted_array, target)
    binary_end = perf_counter()
    binary_time = binary_end - binary_start  # difference in time before and after binary search


    if binary_time < linear_time:
        print("This proves that binary search is more efficient when compared to linear search for searching over large sorted datasets")

sorted_array = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90]
target = 72
search_perf_compare(sorted_array, target)
a = merge_sorted_data()