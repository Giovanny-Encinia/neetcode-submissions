
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
    
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            tmp_node = Node(val=node.val)
            visited[node] = tmp_node
            
            for n in node.neighbors:
                new_node = dfs(n)
                tmp_node.neighbors.append(new_node)
            
            return tmp_node

        graph = dfs(node)

        return graph