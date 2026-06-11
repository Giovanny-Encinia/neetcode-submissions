class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i, t in enumerate(temperatures):
            count = 0
            for y in temperatures[i + 1:len(temperatures)]:
                print(t, y)
                if y > t:
                    count+=1
                    break
                else:
                    count += 1
                
            else:
                count = 0
                    
            result.append(count)
        return result