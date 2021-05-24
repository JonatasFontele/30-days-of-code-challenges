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

    def levelOrder(self, root):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            # Remove it from queue and print front of queue with the pop's return
            node = queue.pop(0)
            print(node.data, end=' ')
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
