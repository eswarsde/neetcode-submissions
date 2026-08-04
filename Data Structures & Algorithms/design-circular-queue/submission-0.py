class MyCircularQueue:

    def __init__(self, k: int):
        # Create a fixed-size array that will store the queue elements.
        # Since this is a circular queue, we reuse these same positions
        # instead of expanding or shrinking the array.
        self.q = [0] * k

        # Store the maximum number of elements the queue can hold.
        self.k = k

        # front points to the index of the current front element.
        #
        # It starts at index 0 because the first inserted element will
        # initially be placed there.
        self.front = 0

        # rear points to the index of the current last element.
        #
        # It starts at -1 because the queue does not contain any elements yet.
        # During the first enqueue:
        #
        # rear = (-1 + 1) % k
        #      = 0
        #
        # Therefore, the first element is inserted at index 0.
        self.rear = -1

        # size tracks how many elements are currently stored in the queue.
        #
        # We use size to distinguish between:
        # - an empty queue: size == 0
        # - a full queue:  size == k
        #
        # This is important because front and rear indexes alone can be
        # ambiguous in a circular queue.
        self.size = 0

    def enQueue(self, value: int) -> bool:
        # If the queue already contains k elements, it is full,
        # so we cannot insert another value.
        if self.isFull():
            return False

        # Move rear forward by one position.
        #
        # The modulo operation wraps rear back to index 0 when it reaches
        # the end of the array.
        #
        # For example, when k = 3:
        # rear = 0 -> 1 -> 2 -> 0 -> 1 ...
        self.rear = (self.rear + 1) % self.k

        # Store the new value at the updated rear position.
        self.q[self.rear] = value

        # Increase the number of elements currently in the queue.
        self.size += 1

        # The insertion was successful.
        return True

    def deQueue(self) -> bool:
        # If the queue contains no elements, there is nothing to remove.
        if self.isEmpty():
            return False

        # Move front forward by one position.
        #
        # We do not need to erase the old value from the array because
        # it is no longer considered part of the logical queue.
        #
        # The modulo operation wraps front back to index 0 when it reaches
        # the end of the array.
        self.front = (self.front + 1) % self.k

        # Decrease the number of elements currently in the queue.
        self.size -= 1

        # The removal was successful.
        return True

    def Front(self) -> int:
        # If the queue is empty, the problem requires us to return -1.
        if self.isEmpty():
            return -1

        # front always points to the first element in the logical queue.
        return self.q[self.front]

    def Rear(self) -> int:
        # If the queue is empty, the problem requires us to return -1.
        if self.isEmpty():
            return -1

        # rear always points to the last element in the logical queue.
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        # The queue is empty when it contains zero elements.
        return self.size == 0

    def isFull(self) -> bool:
        # The queue is full when the current number of elements
        # reaches the maximum capacity.
        return self.size == self.k