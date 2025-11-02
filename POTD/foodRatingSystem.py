class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.mp = dict()
        self.foodRating = dict()
        self.cuisineFood = dict()
        
        for i in range(len(cuisines)):
            cuisine = cuisines[i]
            self.foodRating[foods[i]] = ratings[i]
            self.cuisineFood[foods[i]] = cuisine
            if cuisine not in self.mp:
                self.mp[cuisine] = (ratings[i],foods[i])
            elif ratings[i] > self.mp[cuisine][0]:
                self.mp[cuisine] = (ratings[i],foods[i])
            elif ratings[i] == self.mp[cuisine][0] and foods[i] < self.mp[cuisine][1]:
                self.mp[cuisine] = (ratings[i],foods[i])
        
        


    def changeRating(self, food: str, newRating: int) -> None:
        self.foodRating[food] = newRating
        (oldrating,oldFood) = self.mp[self.cuisineFood[food]] 
        if oldrating < newRating:
            self.mp[self.cuisineFood[food]] = (newRating,food)
        elif oldrating == newRating and food < oldFood:
            self.mp[self.cuisineFood[food]] = (newRating,food)
        elif newRating < oldrating and oldFood == food:
            targetCuisine = self.cuisineFood[food]
            maxFood,maxRating = "",0
            for food,cuisine in self.cuisineFood.items():
                if cuisine == targetCuisine:
                    if self.foodRating[food] > maxRating:
                        maxRating = self.foodRating[food]
                        maxFood = food
                    if self.foodRating[food] == maxRating and maxFood > food:
                        maxRating = self.foodRating[food]
                        maxFood = food
            self.mp[targetCuisine] =(maxRating,maxFood)


    def highestRated(self, cuisine: str) -> str:
        return self.mp[cuisine][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

import heapq
class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foodRating = dict()
        self.foodCuisine = dict()
        self.mp = dict()
        for i in range(len(foods)):
            self.foodRating[foods[i]] = (ratings[i],cuisines[i]) 
            if cuisines[i] not in self.mp:
                self.mp[cuisines[i]] = [(-ratings[i],foods[i])]
            else:
                self.mp[cuisines[i]].append((-ratings[i],foods[i]))
        for cuisine,_ in self.mp.items():
            heapq.heapify(self.mp[cuisine])
    def changeRating(self, food: str, newRating: int) -> None:
        cusine = self.foodRating[food][1]
        self.foodRating[food] = (newRating,cusine)
        heapq.heappush(self.mp[cusine],(-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.mp[cuisine]
        while self.foodRating[heap[0][1]] != heap[0][0]:
            heapq.heappop(heap)
        self.mp[cuisine] = heap
        return heap[0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)