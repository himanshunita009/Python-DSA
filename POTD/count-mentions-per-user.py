from collections import defaultdict
class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        events.sort(key=lambda x: int(x[1]))
        ans = [0]*numberOfUsers
        allCount = 0
        offline = defaultdict(int)
        for event,timestamp,strig in events:
            if event == "MESSAGE":
                if strig == "ALL":
                    allCount += 1
                elif strig == "HERE":
                    for id in range(numberOfUsers):
                        if id not in offline or int(timestamp) - offline[id] > 60:
                            ans[id] += 1
                else:
                    for id in strig.split():
                        id = int(id[2:])
                        ans[id] += 1

            else:
                offline[int(strig)] = int(timestamp)
            if allCount > 0:
                for idx in range(numberOfUsers):
                    ans[idx] += allCount
        return ans

obj = Solution()
print(obj.countMentions(2,[["MESSAGE","10","ALL"],["MESSAGE","15","ALL"]]))