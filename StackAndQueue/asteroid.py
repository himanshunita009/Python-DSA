class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for item in asteroids:
            if item < 0:
                while len(stack) > 0 and stack[-1] < -item:
                    stack.pop()
            stack.append(item)
        return stack 