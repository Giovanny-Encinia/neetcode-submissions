class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        visited = set()

        for right in range(len(nums)):

            if nums[right] not in visited:
                nums[left] = nums[right]
                left += 1
            
            visited.add(nums[right])
        
        return len(visited)
        