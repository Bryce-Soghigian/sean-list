# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            
            curr, level = queue.popleft()
            
            if not curr.left and not curr.right:
                return level
            
            if curr.left:
                queue.append((curr.left, level + 1))
            
            if curr.right:
                queue.append((curr.right, level + 1))
        
        return -1
