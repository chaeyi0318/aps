N = 10
q = [0] * N
front = -1
rear = -1

rear += 1   # enqueue(1)
q[rear] = 1
rear += 1   # enqueue(2)
q[rear] = 2
rear += 1   # enqueue(3)
q[rear] = 3

front += 1      # dequeue()
print(q[front])
front += 1      # dequeue()
print(q[front])
front += 1      # dequeue()
print(q[front])