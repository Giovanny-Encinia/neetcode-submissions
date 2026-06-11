class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i, t in enumerate(temperatures):
            count = 0
            for y in temperatures[i + 1:]:
                count += 1
                if y > t:
                    break
                
                
                
            else:
                count = 0
                    
            result.append(count)
        return result