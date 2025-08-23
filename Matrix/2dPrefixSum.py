class Solution():
    def calcPrefix2DMatrix(self,matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0])
        tempMat = matrix.copy()
        for j in range(1,m):
            tempMat[0][j] += tempMat[0][j-1]
        for i in range(1,n):
            tempMat[i][0] += tempMat[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                tempMat[i][j] = tempMat[i][j] + tempMat[i-1][j] + tempMat[i][j-1] - tempMat[i-1][j-1]
        return tempMat 
        
    def kSubMatrix(self,matrix:list[list[int]],k : int):
        n = len(matrix)
        m = len(matrix[0])
        r2 = c2 = k-1
        while r2 < n:
            c2 = k-1
            while c2 < m:
                r1 = r2 - k +1
                c1 = c2 - k + 1
                sum = matrix[r2][c2] - 0 if r1 < 1 else  matrix[r1-1][c2] - 0 if c1 < 1 else  matrix[r2][c1-1] + 0 if r1 < 1 or c1 < 1 else matrix[r1-1][c1-1]
                print(f"{(r1,c1,r2,c2)} ka sum = {sum}")
                c2 += 1
            r2 += 1

obj = Solution()
temp = obj.calcPrefix2DMatrix([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
print(temp)
obj.kSubMatrix(temp,2)

[
 [0, 1, 2, 3], 
 [1, 3, 5, 7], 
 [1, 4, 7, 10]
 
 ]