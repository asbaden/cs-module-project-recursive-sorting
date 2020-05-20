# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # ^ creating a space to place the merged elements

    # Your code here
    # put this back together 

    a = 0 
    b = 0 
    
    for k in range(0, elements):
        # compare a and b 
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1 
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1 
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        else:
            merged_arr[k] = arrB[b]
            b += 1 

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    
    if len(arr) > 1:
        left = merge_sort(arr[ 0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2: ])

        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    # same as above but use tempory variables to move the variables around, swap values using a tempory variable
    # Merges two subarrays of arr. 
    # First subarray is arr[l..m] 
    # Second subarray is arr[m+1..r] 
    # Inplace Implementation 
    #start of second array
    start2 = mid + 1 
    # two pointers to maintain start 
    while (start <= mid and start2 <= end):
        if (arr[start] <= arr[start2]):
            start += 1 
        else:
            value = arr[start2]
            index = start2
            #shift all the elements between element 1
            #element 2, right by 1
            while(index is not start):
                arr[index] = arr[index - 1]
                index -= 1 
            
            arr[start] = value

            #update all the pointers
            start += 1 
            mid += 1
            start2 += 1


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):
        m = l + (r-l) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l , m , r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
