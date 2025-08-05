class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        temp = dict()
        n = len(fruits)
        ans = 0
        for i in range(n):
            if fruits[i] in temp:
                temp[fruits[i]] += 1
            else :
                if len(temp) == 2:
                    sum = 0
                    first = -1
                    second = -1
                    for key,value in temp:
                        sum += value
                        if first == -1:
                            first = key
                        else :
                            second = key
                    ans = max(ans,sum)
                    if fruits[i-1] == first:
                        temp.pop(second)
                    else:
                        temp.pop(first)
                temp[fruits[i]] = 1
        sum  =0
        for key,value in temp:
            sum += value 
        return max(ans,sum)
        
                