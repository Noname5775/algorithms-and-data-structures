class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        # Фиктивная голова для упрощения операций
        self.head = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        # Проверка на корректность индекса
        if index < 0 or index >= self.length:
            return -1

        current = self.head.next
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # Если индекс больше длины, вставка невозможна
        if index < 0 or index > self.length:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        # Если индекс неверный, ничего не делаем
        if index < 0 or index >= self.length:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        # Пропускаем удаляемый узел
        prev.next = prev.next.next
        self.length -= 1