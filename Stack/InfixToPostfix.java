public class InfixToPostfix {

    static class CharStack {
        private char[] arr;
        private int top;
        private int capacity;

        public CharStack(int capacity) {
            this.capacity = capacity;
            this.arr = new char[capacity];
            this.top = -1;
        }

        public void push(char c) {
            if (isFull()) {
                System.out.println("Stack Overflow: cannot push " + c);
                return;
            }
            top++;
            arr[top] = c;
        }

        public char pop() {
            if (isEmpty()) {
                System.out.println("Stack Underflow: stack is empty");
                return '\0';
            }
            char val = arr[top];
            top--;
            return val;
        }

        public char peek() {
            if (isEmpty()) {
                return '\0';
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
    }

    public static int precedence(char op) {
        switch (op) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
            default:
                return -1;
        }
    }

    public static boolean isRightAssociative(char op) {
        return op == '^';
    }

    public static String convert(String infix) {
        StringBuilder postfix = new StringBuilder();
        CharStack stack = new CharStack(infix.length());

        for (int i = 0; i < infix.length(); i++) {
            char c = infix.charAt(i);

            if (c == ' ') {
                continue;
            }

            if (Character.isLetterOrDigit(c)) {
                postfix.append(c);
            } else if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfix.append(stack.pop());
                }
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    System.out.println("Error: Mismatched parentheses!");
                }
            } else if (precedence(c) > 0) {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    int topPrec = precedence(stack.peek());
                    int currPrec = precedence(c);

                    if ((!isRightAssociative(c) && topPrec >= currPrec) ||
                        (isRightAssociative(c) && topPrec > currPrec)) {
                        postfix.append(stack.pop());
                    } else {
                        break;
                    }
                }
                stack.push(c);
            }
        }

        while (!stack.isEmpty()) {
            char top = stack.pop();
            if (top == '(') {
                System.out.println("Error: Mismatched parentheses!");
            } else {
                postfix.append(top);
            }
        }

        return postfix.toString();
    }
}
