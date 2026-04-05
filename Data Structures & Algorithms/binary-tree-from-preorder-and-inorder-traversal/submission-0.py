# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # pre-order: root -> left -> right
        # inorder: left -> root -> right

        q = deque(preorder)

        def dfs(in_ord):

            if not in_ord:
                return None

            root_val = q.popleft()

            for i, n in enumerate(in_ord):
                print(n, root_val)
                if n == root_val:
                    left = in_ord[:i]
                    right = in_ord[i+1:]
                    break

            return TreeNode(root_val, dfs(left), dfs(right))
        
        return dfs(inorder)


        # first element in preorder is root
        # find root in inorder
        # everything before that is left of root
        # everything after is right of the root

        # second element in preorder will be 'root' now

