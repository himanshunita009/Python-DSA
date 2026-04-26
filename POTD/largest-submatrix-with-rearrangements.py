class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        ans = 1
        histogram = [0]*len(matrix[0])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    histogram[col] = 0
                else:
                    histogram[col] += 1
            histogram.sort(reverse=True)
            for idx in range(len(histogram)):
                if histogram[idx] == 0:
                    break
                ans = max(ans,histogram[idx]*(idx+1))
        return ans
obj = Solution()
print(obj.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]))
