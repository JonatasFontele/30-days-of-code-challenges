class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root is None:
            # -1 if edges, 0 if nodes
            return -1
        else:
            # Compute the depth of each subtree
            left_depth = self.getHeight(root.left)
            right_depth = self.getHeight(root.right)
            # Use the larger one 
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
