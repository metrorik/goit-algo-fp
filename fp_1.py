class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Функція для вставки нового вузла на початок списку
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Функція для вставки нового вузла в кінець списку
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Функція для вставки нового вузла після заданого вузла
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Функція для видалення вузла за значенням ключа
    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    # Функція для пошуку елемента у списку
    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Функція для друку списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція для реверсування однозв'язного списку
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    # Функція для злиття двох відсортованих однозв'язних списків в один відсортований список
    def sorted_merge(self, other):
        p = self.head
        q = other.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head

    # Функція для сортування однозв'язного списку методом вставки
    def insertion_sort(self):
        sorted_list = LinkedList()
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = None
            sorted_list.sorted_insert(cur)
            cur = next_node
        self.head = sorted_list.head

    # Допоміжна функція для вставки вузла у відсортований список
    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur.next and cur.next.data < new_node.data:
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node

# Приклад використання:
llist = LinkedList()
llist.insert_at_end(15)
llist.insert_at_end(10)
llist.insert_at_end(5)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Оригінальний список:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("Реверсований список:")
llist.print_list()

# Сортування списку методом вставки
llist.insertion_sort()
print("Відсортований список:")
llist.print_list()

# Об'єднання з іншим відсортованим списком
llist2 = LinkedList()
llist2.insert_at_end(7)
llist2.insert_at_end(12)
llist2.insert_at_end(17)

llist.sorted_merge(llist2)
print("Об'єднаний відсортований список:")
llist.print_list()
