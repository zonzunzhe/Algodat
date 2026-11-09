public class Stack {
    private int[] arr;
    private int capacity;
    private int top;

    public Stack(int size) {
        this.capacity = size;
        this.arr = new int[capacity];
        this.top = -1;
    }

    public void push(int value) {
        if (isFull()) {
            System.out.println("[Stack Overflow] Tidak dapat melakukan push " + value + " (Stack sudah penuh).");
            return;
        }

        top++;
        arr[top] = value;
        System.out.println("Berhasil push ke Stack: " + value);
    }

    public int pop() {
        if (isEmpty()) {
            System.out.println("[Stack Underflow] Tidak dapat melakukan pop (Stack kosong).");
            return -1;
        }

        int value = arr[top];
        top--;
        System.out.println("Berhasil pop dari Stack: " + value);
        return value;
    }

    public int peek() {
        if (isEmpty()) {
            System.out.println("[Stack Info] Stack kosong, tidak ada elemen untuk di-peek.");
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
            System.out.println("Stack: [ Kosong ]");
            return;
        }

        System.out.println("Isi Stack saat ini (puncak ke dasar):");
        for (int i = top; i >= 0; i--) {
            if (i == top) {
                System.out.println("| " + arr[i] + " | <-- TOP");
            } else {
                System.out.println("| " + arr[i] + " |");
            }
        }
        System.out.println("-------");
    }
}
