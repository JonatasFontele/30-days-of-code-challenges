class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class without constructor
class Solution:
    @staticmethod
    def display(head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    @staticmethod
    def insert(head, data):
        new_node = Node(data)
        if head is None:
            head = new_node
            return head
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head


def main():
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)


if __name__ == "__main__":
    main()
