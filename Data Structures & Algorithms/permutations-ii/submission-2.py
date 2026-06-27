class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_perm = []
        index = 0
        set_index = set()
        def permutation(current_perm, set_index):
            if len(current_perm) == len(nums) and current_perm not in result:
                #print("condicion cumpplidda", current_perm)
                result.append(current_perm[:])
                return None
            #print("set index", set_index)
            i = 0
            while i < len(nums):
                #print(nums[i], i)
                if i not in set_index:
                    #print("prosigue")
                    current_perm.append(nums[i])
                    set_index.add(i)
                    #print("prosigue", current_perm)
                    permutation(current_perm, set_index)
                    set_index.remove(i)
                    current_perm.pop()
                
                
                i += 1
        
        permutation(current_perm, set_index)
        return result