"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        cloned = {}
        
        def clone(node):

            if node in cloned:
                return cloned[node]

            if not node:
                return None

            cloned[node] = Node(node.val, [])
        
            for n in node.neighbors:
                cloned[node].neighbors.append(clone(n))
                
            return cloned[node]

        return clone(node)
        

        