class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        temp1 = 0
        temp2 = 0
        v1 = len(version1)
        v2 = len(version2)
        n = max(v1,v2)
        for i in range(n):
            if i < v1:
                temp1 = int(version1[i])
            else:
                temp1 = 0
            if i < v2:
                temp2 = int(version2[i])
            else:
                temp2 = 0
            if temp1 < temp2:
                return -1
            elif temp1 > temp2:
                return 1
        return 0
