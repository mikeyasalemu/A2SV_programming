# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque()
        queue.append(root)
        parent = {}

        while queue:

            size = len(queue)

            for _ in range(size):
                top = queue.popleft()

                if top.right:
                    parent[top.right.val] = top
                    queue.append(top.right)
                if top.left:
                    parent[top.left.val] = top
                    queue.append(top.left)

        vis = set()
        queue.append(target)
        vis.add(target.val)
        while k > 0 and queue:
            size = len(queue)

            for _ in range(size):
                cur = queue.popleft()

                if  cur.right and cur.right.val not in vis:
                    queue.append(cur.right)
                    vis.add(cur.right.val)
                if  cur.left and cur.left.val not in vis:
                    queue.append(cur.left)
                    vis.add(cur.left.val)
                if cur.val in parent and parent[cur.val].val not in vis:
                    queue.append(parent[cur.val])
                    vis.add(parent[cur.val].val)
            k -=1
        
        ans = []
        while queue:
            ans.append(queue.popleft().val)
        
        return ans