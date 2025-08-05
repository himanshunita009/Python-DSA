class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        usedBaskets = 0
        for fruit in fruits:
            for idx in range(len(baskets)):
                if baskets[idx] == -1 or baskets[idx] < fruit:
                    continue
                else:
                    baskets[idx] = -1
                    usedBaskets+= 1
                    break
        return len(fruits)-usedBaskets
    

