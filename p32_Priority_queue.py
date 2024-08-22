"""Prioritná fronta

Zadanie:
Implementujte frontu, ktorá dokáže spracovávať priotitné prvky.
Prioritné prvky by mali bať vždy spracované pred ne-prioritnými prvkami,
pričom poradie v rámci prioritnej alebo ne-prioritnej fronty by malo byť FIFO.

prioritné1 neprioritné1 neprioritné2 prioritné2
-> prioritné1 prioritné2 neprioritné1 neprioritné2
"""

from collections import deque
class PriorityQueue:
    def __init__(self):
        self.normal_queue = deque()
        self.priority_queue = deque()

    def enqueue(self, item, priority=False):
        if priority:
            self.priority_queue.append(item)
        else:
            self.normal_queue.append(item)

    def dequeue(self):
        if self.priority_queue:
            return self.priority_queue.popleft()
        elif self.normal_queue:
            return self.normal_queue.popleft()
        raise IndexError("Queue is empty")

if __name__ == '__main__':
    queue = PriorityQueue()
    queue.enqueue("normal task 1")
    queue.enqueue("normal task 2")
    queue.enqueue("priority task 1", True)
    queue.enqueue("priority task 2", True)
    queue.enqueue("normal task 3")
    queue.enqueue("normal task 4")

    print(queue.dequeue())  # "priority task 1"
    print(queue.dequeue())  # "priority task 2"
    print(queue.dequeue())  # "normal task 1"
    print(queue.dequeue())  # "normal task 2"
    print(queue.dequeue())  # "normal task 3"
    print(queue.dequeue())  # "normal task 4"
