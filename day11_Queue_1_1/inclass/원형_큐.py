Q_SIZE = 4
cQ = [0] * 4
front = 0
rear = 0

rear = (rear + 1) % Q_SIZE  # enqueue(1)
cQ[rear] = 1

rear = (rear + 1) % Q_SIZE  # enqueue(2)
cQ[rear] = 2

rear = (rear + 1) % Q_SIZE  # enqueue(3)
cQ[rear] = 3

front = (front + 1) % Q_SIZE
print(cQ[front])

front = (front + 1) % Q_SIZE
print(cQ[front])

front = (front + 1) % Q_SIZE
print(cQ[front])