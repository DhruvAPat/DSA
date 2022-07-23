def SelectionSort(arr):
    l=len(arr)
    for i in range(l):
        min=i
        for j in range(i+1,l):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr



arr=[23,1,34,12,3,44]
z=SelectionSort(arr)
print("The sorted array is", z)
