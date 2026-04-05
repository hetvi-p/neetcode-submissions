# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        l = []

        def inorder(node):

            if node:
                left = inorder(node.left)
                if left is not None:
                    return left

                l.append(node.val)
                if len(l) == k:
                    return node.val

                return inorder(node.right)

        return inorder(root)




        def useStack(root):

            stack = []
            curr = root
            count = 1

            while stack or curr:
                
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop() # could be None
                # process
                
                if count == k:
                    return curr.val
                else:
                    count += 1

                curr = curr.right

        return useStack(root)



