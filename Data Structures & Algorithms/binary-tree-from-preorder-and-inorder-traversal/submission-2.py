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

        # store index of node in hashmap

        in_map = {}

        for i, n in enumerate(inorder):
            in_map[n] = i

        pre_ind = 0

        def dfs(sta, end):

            nonlocal pre_ind

            if not inorder[sta:end]:
                return None

            root_val = preorder[pre_ind]

            i = in_map[root_val]
            pre_ind += 1

            return TreeNode(root_val, dfs(sta, i),
                    dfs(i+1, end))
        
        return dfs(0, len(inorder))


        # first element in preorder is root
        # find root in inorder
        # everything before that is left of root
        # everything after is right of the root

        # second element in preorder will be 'root' now

