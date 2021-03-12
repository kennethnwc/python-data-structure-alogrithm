
A = [2,4,1,6,8,5,3,7]

# O(n**2)
def bubble_sort(arr):
    n = len(arr)
    for k in range(1, n):
        need_sort = 0
        for i in range(n-k):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                need_sort = 1
        if not need_sort:
            break
    return arr

# O(n**2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[min_i], arr[i] = arr[i], arr[min_i]
    
    return arr
    

# O(n**2)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        hole = i
        while hole > 0 and arr[hole-1] > curr:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = curr
    
    return arr

# O(n log n)        
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        # merge 
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Quick sort
# O ( n log n)
def partition(arr, low, high):
    
    pivot_num = arr[high]
    partition_index = low
    for i in range(low, high):
        if arr[i] <= pivot_num:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1
            
    arr[partition_index],arr[high] = arr[high], arr[partition_index]
    return partition_index

def _quick_sort(arr, low, high):
    if low >= high:
        return
    pivot = partition(arr, low, high)
    _quick_sort(arr, low, pivot-1)
    _quick_sort(arr, pivot + 1, high)

def quick_sort(arr):
    low = 0
    high = len(arr) - 1
    _quick_sort(arr, low, high)
    return arr
    



# bubble_sort(A)
# selection_sort(A)
# insertion_sort(A)
# merge_sort(A)
quick_sort(A)

