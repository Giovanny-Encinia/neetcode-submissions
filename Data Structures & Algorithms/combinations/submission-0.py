class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        c(n, k) you need to create a list from 1 to n
        find the combinations
        add 1 or not add 1 then 1->2 or 1->[] and []->2 or []->[] 
        there is no a list but we have the info in the nmber, imagine i
        is a sorted list
        """
        def dfs(result, current_comb, index, n, k):
            if len(current_comb) == k:
                result.append(current_comb.copy())
                return
            if index > n:
                return None
                
            current_comb.append(index)
            dfs(result, current_comb, index + 1, n, k)
            current_comb.pop()
            dfs(result, current_comb, index + 1, n, k)
            
        result = []
        current_comb = []
        dfs(result, current_comb, 1, n, k)
        return result
