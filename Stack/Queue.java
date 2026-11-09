public class Queue {
    private int[] arr;
    private int capacity;
    private int front;
    private int rear;
    private int count;

    public Queue(int size) {
        this.capacity = size;
        this.arr = new int[capacity];
        this.front = 0;
        this.rear = -1;
        this.count = 0;
    }

    public void enqueue(int value) {
        if (isFull()) {
            System.out.println("[Queue Overflow] Cannot enqueue " + value + " (Queue is full).");
            return;
        }

        rear = (rear + 1) % capacity;
        arr[rear] = value;
        count++;
        System.out.println("Enqueued: " + value);
    }

    public int dequeue() {
        if (isEmpty()) {
            System.out.println("[Queue Underflow] Cannot dequeue (Queue is empty).");
            return -1;
        }

        int value = arr[front];
        front = (front + 1) % capacity;
        count--;
        System.out.println("Dequeued: " + value);
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("[Queue Info] Queue is empty, cannot peek.");
            return -1;
        }

        return arr[front];
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public boolean isFull() {
        return count == capacity;
    }

    public int size() {
        return count;
    }

    public void printQueue() {
        if (isEmpty()) {
            System.out.println("Queue: [ Empty ]");
            return;
        }

        System.out.print("Queue (FRONT -> REAR): [ ");
        for (int i = 0; i < count; i++) {
            int index = (front + i) % capacity;
            System.out.print(arr[index]);
            if (i < count - 1) {
                System.out.print(" -> ");
            }
        }
        System.out.println(" ] (Size: " + count + "/" + capacity + ")");
    }
}
