class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Функція для реверсування списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Функція для поділу списку на дві частини
def split_list(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return head, mid

# Функція для злиття двох відсортованих списків
def merge_lists(left, right):
    dummy = ListNode()
    tail = dummy
    while left and right:
        if left.value < right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    if left:
        tail.next = left
    if right:
        tail.next = right
    return dummy.next

# Функція для сортування злиттям
def merge_sort(head):
    if not head or not head.next:
        return head
    left, right = split_list(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_lists(left, right)

# Допоміжна функція для створення списку зі списку значень
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Допоміжна функція для виведення списку
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Приклад використання
values = [4, 2, 1, 3]
head = create_linked_list(values)
print("Original list:")
print_list(head)

# Реверсування списку
reversed_head = reverse_list(head)
print("Reversed list:")
print_list(reversed_head)

# Сортування списку
sorted_head = merge_sort(reversed_head)
print("Sorted list:")
print_list(sorted_head)

# Об'єднання двох відсортованих списків
list1 = create_linked_list([1, 3, 5])
list2 = create_linked_list([2, 4, 6])
merged_head = merge_lists(list1, list2)
print("Merged sorted lists:")
print_list(merged_head)