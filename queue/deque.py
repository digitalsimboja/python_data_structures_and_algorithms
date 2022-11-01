from collections import deque
import queue as q
from multiprocessing import Queue as mult

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue.popleft())

print(customQueue)
customQueue.clear()

cusQ = q.Queue(maxsize=3)
print(cusQ.empty())
cusQ.put(1)
cusQ.put(2)
cusQ.put(3)

print(cusQ.get())

multQ = mult(maxsize=3)
print(multQ.empty())