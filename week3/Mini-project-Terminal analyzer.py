def bubble_sort(arr):
    print(f" Initial: {arr}")
    for i in range(len(arr)-1):
        swapped=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(f'swap: {arr}') 
                swapped=True

        if not swapped:
            break
    print(f"Sorted: {arr}") #To confirm the ouput in human-readable form(eg. initial,swap,sorted)
    return arr #To print the actual list if needed to be used further
arr=[5, 2, 4, 1, 8, 3]

print(bubble_sort(arr)) 