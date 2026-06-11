class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        tem = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                value, prev_i = stack.pop()
                tem[prev_i] = i - prev_i

            stack.append((t, i))

        return tem