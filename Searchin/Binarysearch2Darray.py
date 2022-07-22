def search2DSortedMatrix(matrix,target):
    i=0
    j=len(matrix[0])-1
    n=len(matrix)
    while(i<n & j>=0):
        if matrix[i][j]==target:
            return True
        elif matrix[i][j]>target:
            j-=1
        else:
            i+=1
    return False
matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = int(input("Enter the Number to be searched"))
result = search2DSortedMatrix(matrix, target)
print("Result is", result)