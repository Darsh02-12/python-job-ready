def bubble_sort(arr):
    
    for i in range(len(arr)-1):
        swapped=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j] 
                swapped=True

        if not swapped:
            break
    return arr

arr=[5, 2, 4, 1, 8, 3]

print(bubble_sort(arr)) 

# testing stash