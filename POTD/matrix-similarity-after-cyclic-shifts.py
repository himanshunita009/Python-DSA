class Solution:
    def rotate(self,arr :list[int],step: int):
        for idx in range(step//2):
            arr[idx],arr[step-1-idx] = arr[step-1-idx],arr[idx]
        for idx in range((len(arr)-step)//2):
            arr[step+idx],arr[len(arr)-1-idx] = arr[len(arr)-1-idx],arr[step+idx]
        arr.reverse()
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        m = len(mat[0])
        k = k%m
        for idx in range(len(mat)):
            temp = mat[idx].copy()
            if idx&1:
                self.rotate(mat[idx],m-k)
            else:
                self.rotate(mat[idx],k)
            if mat[idx] != temp:
                return False
        return True
        
        