public class Main {
    public static void main(String[] args) {
        System.out.println("======================================================");
        System.out.println("  DATA STRUCTURE DEMONSTRATION: INFIX/POSTFIX & QUEUE ");
        System.out.println("======================================================\n");

        System.out.println("------------------------------------------------------");
        System.out.println(">>> 1. INFIX TO POSTFIX CONVERSION <<<");
        System.out.println("------------------------------------------------------");

        String[] expressions = {
            "A + B * C",
            "(A + B) * C",
            "A + B * (C ^ D - E) ^ (F + G * H) - I",
            "((A + B) * C - (D - E)) ^ (F + G)",
            "a + b * c / d - e",
            "K + L - M * N + (O ^ P) * W / U / V * T + Q"
        };

        for (int i = 0; i < expressions.length; i++) {
            String infix = expressions[i];
            String postfix = InfixToPostfix.convert(infix);
            System.out.println("Expression " + (i + 1) + ":");
            System.out.println("  Infix   : " + infix);
            System.out.println("  Postfix : " + postfix);
        }

        System.out.println("\n------------------------------------------------------");
        System.out.println(">>> 2. QUEUE DEMONSTRATION (Capacity: 5 - Circular) <<<");
        System.out.println("------------------------------------------------------");

        Queue queue = new Queue(5);
        System.out.println("Initial queue empty? " + queue.isEmpty());

        System.out.println("\n[A] Enqueue 5 Elements:");
        queue.enqueue(100);
        queue.enqueue(200);
        queue.enqueue(300);
        queue.enqueue(400);
        queue.enqueue(500);

        System.out.println("\n[B] Current Queue State:");
        queue.printQueue();

        System.out.println("\n[C] Peek & Size Check:");
        System.out.println("Front element : " + queue.peek());
        System.out.println("Current size  : " + queue.size());
        System.out.println("Is full?      : " + queue.isFull());

        System.out.println("\n[D] Queue Overflow Test (Enqueue when full):");
        queue.enqueue(600);

        System.out.println("\n[E] Dequeue 2 Elements:");
        queue.dequeue();
        queue.dequeue();

        System.out.println("\n[F] Current Queue State after 2 Dequeues:");
        queue.printQueue();

        System.out.println("\n[G] Circular Array Wrap-Around Test:");
        System.out.println("Enqueue 600 and 700 to reuse empty front slots:");
        queue.enqueue(600);
        queue.enqueue(700);
        queue.printQueue();
        System.out.println("Is queue full again? " + queue.isFull());

        System.out.println("\n[H] Emptying Queue:");
        while (!queue.isEmpty()) {
            queue.dequeue();
        }
        System.out.println("Queue empty now? " + queue.isEmpty());

        System.out.println("\n[I] Queue Underflow Test (Dequeue when empty):");
        queue.dequeue();

        System.out.println("\n======================================================");
        System.out.println("               DEMONSTRATION FINISHED                 ");
        System.out.println("======================================================");
    }
}
