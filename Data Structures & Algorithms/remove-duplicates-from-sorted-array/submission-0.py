class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        visited = set()

        for right in range(len(nums)):

            if nums[right] in visited:
                pass
            else:
                nums[left] = nums[right]
                left += 1
            
            visited.add(nums[right])
        
        return len(visited)
        