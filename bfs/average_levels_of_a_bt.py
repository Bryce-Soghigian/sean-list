# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        
        
        queue = deque([root])
        while queue:
            avg = 0
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                
                avg += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                    
            output.append(avg/size)
        return output
