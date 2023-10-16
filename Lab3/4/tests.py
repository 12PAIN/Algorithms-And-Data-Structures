from lists.Stack import Stack
from lists.Queue import Queue
from lists.Deque import Deque

st = Stack()
print("!!!ТЕСТИРОВАНИЕ СТЕКА!!!")
print()

print("PUSH 4")
print(st.push(4))
print(st)
print()

print("PUSH DOG")
print(st.push('dog'))
print(st)
print()

print("PEEK ")
print(st.peek())
print(st)
print()

print("PUSH TRUE")
print(st.push(True))
print(st)
print()

print("POP")
print(st.pop())
print(st)
print()

print("POP")
print(st.pop())
print(st)
print()

qu = Queue()
print("!!!ТЕСТИРОВАНИЕ ОЧЕРЕДИ!!!")
print()

print("ENQUEUE 4")
print(qu.enqueue(4))
print(qu)
print()

print("ENQUEUE DOG")
print(qu.enqueue("dog"))
print(qu)
print()

print("ENQUEUE TRUE")
print(qu.enqueue(True))
print(qu)
print()

print("DEQUEUE")
print(qu.dequeue())
print(qu)
print()

print("DEQUEUE")
print(qu.dequeue())
print(qu)
print()

dq = Deque()
print("!!!ТЕСТИРОВАНИЕ ДЕКА!!!")
print()

print("ADD REAR 4")
print(dq.addRear(4))
print(dq)
print()

print("ADD REAR DOG")
print(dq.addRear("dog"))
print(dq)
print()

print("ADD FRONT CAT")
print(dq.addFront("cat"))
print(dq)
print()

print("ADD FRONT TRUE")
print(dq.addFront(True))
print(dq)
print()

print("REMOVE REAR")
print(dq.removeRear())
print(dq)
print()

print("REMOVE FRONT")
print(dq.removeFront())
print(dq)
print()
