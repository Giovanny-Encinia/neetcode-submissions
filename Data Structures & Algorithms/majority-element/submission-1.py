from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count_element = defaultdict(int)

        for n in nums:
            count_element[n] += 1

            if count_element[n] > len(nums) // 2:
                return n
        
