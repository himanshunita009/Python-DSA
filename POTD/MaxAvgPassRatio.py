import heapq
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def gain(p,q):
            return (p+1)/(q+1) - p/q
        heap = [(-gain(p,q),p,q) for p,q in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            max_gain,p,q = heapq.heappop(heap)
            p,q = p+1,q+1
            heapq.heappush(heap,(-gain(p,q),p,q))
        total = sum(p/q for _,p,q in heap)
        return total / len(classes)             
        