from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(int)

        for i, n in enumerate(nums):
            difference = target - n

            if difference in nums_dict:
                return list((nums_dict[difference], i))
            
            nums_dict[n] = i
        