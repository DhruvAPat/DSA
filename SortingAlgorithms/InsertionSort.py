def insertionsort(arr):
    
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr=[75,90,100,95,85,50,102,110]
print("The Sorted Array is",insertionsort(arr))