class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_length = float("inf")
        left = 0
        total_sum = 0

        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                min_length = min(min_length, right - left + 1)
                total_sum -= nums[left]
                left += 1
            
        
        return min_length if min_length != float("inf") else 0