class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        i , j = 0,0
        ans = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
            j += 1
        return ans

obj = Solution()
print(obj.matchPlayersAndTrainers([1,1,1],[10]))