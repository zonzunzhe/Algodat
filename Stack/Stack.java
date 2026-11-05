public class Stack {
    int[] arr;
    int capacity;
    int top;

    public Stack(int size) {
        capacity = size;
        arr = new int[capacity];
        top = -1;
    }

    public void push(int value) {
        if (isFull()) {
            System.out.println("Stack Overflow! Cannot push " + value + " (Stack is full)");
            return;
        }

        top++;
        arr[top] = value;
        System.out.println("Pushed " + value + " to stack");
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Underflow! Cannot pop (Stack is empty)");
            return -1;
        }

        int value = arr[top];
        top--;
        System.out.println("Popped " + value + " from stack");
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty! Nothing to peek");
            return -1;
        }

        return arr[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == capacity - 1;
    }

    public int size() {
        return top + 1;
    }

    public void printStack() {
        if (isEmpty()) {
            System.out.println("Stack is empty!");
            return;
        }

        System.out.println("Current Stack (top to bottom):");
        for (int i = top; i >= 0; i--) {
            System.out.println("| " + arr[i] + " |");
        }
        System.out.println("-------");
    }

    public static void main(String[] args) {
        System.out.println("--- Stack Demo for Beginners ---\n");

        Stack stack = new Stack(4);
        System.out.println("Created stack with capacity 4.");
        System.out.println("Is stack empty? " + stack.isEmpty());

        System.out.println("\n--- Pushing elements ---");
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("\n--- Printing Stack ---");
        stack.printStack();

        System.out.println("\n--- Peeking ---");
        System.out.println("Top element is: " + stack.peek());
        System.out.println("Stack size is: " + stack.size());

        System.out.println("\n--- Testing Overflow ---");
        stack.push(40);
        System.out.println("Is stack full? " + stack.isFull());
        stack.push(50);

        System.out.println("\n--- Popping elements ---");
        stack.pop();
        stack.pop();
        stack.printStack();

        System.out.println("\n--- Testing Underflow ---");
        stack.pop();
        stack.pop();
        System.out.println("Is stack empty? " + stack.isEmpty());
        stack.pop();
    }
}
