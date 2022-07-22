def search(arr,r,l,s):
    if r==l:
        if arr[r]==s:
            return r
        else:
            return -1
    else:
        mid=r+(l-r)//2
        if arr[mid]==s:
            return mid
        elif arr[mid]<s:
            return search(arr,mid+1,l,s)
        else:
            return search(arr,r,mid-1,s)

arr=[12,14,45,56,67,70,80]

r=0
l=len(arr)
s=int(input("Enter element to be searched"))
print(search(arr,r,l,s))