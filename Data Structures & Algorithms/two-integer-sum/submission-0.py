
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        history = {}
        for i, n in enumerate(nums):
            complement = target - n

            if complement in history:
                return [history[complement], i]

            history[n] = i

        

        