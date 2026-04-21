'''
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
'''
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    def levelOrder(root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
        
        
    if root == []:
        return []

    # Perform level order traversal and get the nodes in each level
    levels = levelOrder(root)

    # return last index from each level 
    result = []
    for level in levels:
        result.append(level[-1])

    return result

print(rightSideView(None))
print(rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))))
print(rightSideView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))
print(rightSideView(TreeNode(1, None, TreeNode(2))))


'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to return the left side view instead of the right side view?
2. Can you solve this problem using DFS instead of BFS? What are the trade-offs?
3. What if we need to find both left and right side views in a single traversal?

=== REAL WORLD APPLICATION ===
Computer Graphics and Rendering: Used in 3D graphics engines to determine which objects are visible from a specific camera viewpoint. This helps optimize rendering by only drawing visible surfaces, similar to how only right-side nodes are "visible" from the right perspective.

File System Navigation: In hierarchical file systems, this algorithm helps determine what folders/files are visible when viewing a directory tree from a specific angle or in tree-view UI components, ensuring only the relevant items are displayed to the user.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Each node is visited exactly once during BFS traversal
- Queue operations (enqueue/dequeue) are O(1) each
- Processing nodes at each level requires O(nodes_in_level) operations
- Total time is proportional to the number of nodes in the tree

Space Complexity: O(w) where w is the maximum width of the tree
- In the worst case (complete binary tree), the maximum width is n/2 (leaf level)
- Queue stores at most one level of nodes at any time
- For a skewed tree, space complexity becomes O(1)
- For a balanced tree, space complexity is O(n) in the worst case
'''