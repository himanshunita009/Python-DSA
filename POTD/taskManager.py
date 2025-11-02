import heapq
class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.mp = []
        self.taskUser = dict() 
        for [userId,taskId,priority] in tasks:
            self.mp.append((-priority,-taskId,userId))
            self.taskUser[taskId] = (userId,priority)
        heapq.heapify(self.mp)
    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.mp,(-priority,-taskId,userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.taskUser[taskId][0]
        self.taskUser[taskId] = (userId,newPriority)
        heapq.heappush(self.mp,(-newPriority,-taskId,userId))

    def rmv(self, taskId: int) -> None:
        self.taskUser.pop(taskId)        

    def execTop(self) -> int:
        while self.taskUser[-self.mp[0][1]] != -self.mp[0][0]:
            heapq.heappop(self.mp)
        if len(self.mp) == 0:
            return -1
        userId = self.mp[0][2]
        heapq.heappop(self.mp)
        return userId
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()