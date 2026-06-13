class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left = 0
        visited = set()
        
        for right in range(len(nums)):

            if right - left > k:
                visited.remove(nums[left])
                left += 1
                
            if nums[right] in visited:
                return True

            visited.add(nums[right])

        return False
