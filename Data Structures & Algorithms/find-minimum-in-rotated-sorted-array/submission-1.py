class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        local_min = float("inf")
        global_min = local_min

        while left <= right:
            mid = (left + right) // 2
            
            # is left ordered?
            if nums[left] <= nums[mid]:
                local_min = nums[left]
                left = mid + 1
                # move to right to search another minimal    
            # search in the right ordered
            else:
                local_min = nums[mid]
                right = mid - 1

            global_min = min(global_min, local_min)
        return global_min

            