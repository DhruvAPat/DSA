from re import L


def bubblesort(arr):
    l=len(arr)
    for i in range(l):
        #In the Second loop we exclude the rightmost elements in each comparison as the rightmost ones are 
        #already sorted.
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr




arr=[2,123,14,32,1212,34,56,12,33,5]
z=bubblesort(arr)
print("The Sorted Array is",z)