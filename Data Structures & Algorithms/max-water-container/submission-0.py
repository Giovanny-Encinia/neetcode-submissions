class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:

            h_r = heights[right]
            h_l = heights[left]

            base = right - left
            h = min(heights[right], heights[left])
            current_area = base * h

            if h_l < h_r:
                left += 1
            else:
                right -= 1
            
            max_area = max(max_area, current_area)
        
        return max_area
