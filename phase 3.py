import random

def generate_sorted_data(size):
    random.seed(0)
    
    
    #data = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90] + [random.randint(1, 100) for _ in range((990))]
    data = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90]
    merge_sort(data, 0, len(data) - 1)
    return data
    

def merge_sort(array, start, end):
    if start < end:
       mid= (start + end) // 2
       merge_sort(array, start, mid)
       merge_sort(array, mid + 1, end)
       
       merge_sec(array, start, mid, end)


def merge_sec(array, start, mid, end):
    leftsize = mid - start + 1
    rightsize = end - mid

    leftpart = [0] * leftsize
    rightpart = [0] * rightsize

    for i in range(leftsize):
        leftpart[i] = array[start + i]
    for j in range(rightsize):
        rightpart[j] = array[mid + 1 + j]

    i = j = 0 
    k = start  

    while i < leftsize and j < rightsize:
        if leftpart[i] <= rightpart[j]:
            array[k] = leftpart[i]
            i += 1
        else:
            array[k] = rightpart[j]
            j += 1
        k += 1
        
    while i < leftsize:
        array[k] = leftpart[i]
        i += 1
        k += 1

    while j < rightsize:
        array[k] = rightpart[j]
        j += 1
        k += 1

large_data = generate_sorted_data(1000)
print("First 10 elements after sorting:", large_data[:10])