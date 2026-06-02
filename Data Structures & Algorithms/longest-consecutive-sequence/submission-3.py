class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        size = 1
        repeated = set()
        max_len = 1

        if not nums:
            return 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] +  1 == nums[i + 1]:
                size += 1
                print(True)
            else:
                size = 1
            
            max_len = max(size, max_len)
            
        
        return max_len


        