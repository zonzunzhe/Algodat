# Beginner-Friendly Java Stack Implementation & Guide

A simple, beginner-friendly implementation of a **Stack** data structure in Java using a standard fixed-size array (`int[]`), designed specifically for students and junior developers learning Data Structures (Algodat).

---

## 📁 Files in This Project

* [**`Stack.java`**](file:///C:/Kuliah/Semester%203/Algodat/Stack/Stack.java): Clean, straightforward Java code implementing an array-based stack with a simple test in `main()`.
* [**`Java_Stack_Junior_Guide.docx`**](file:///C:/Kuliah/Semester%203/Algodat/Stack/Java_Stack_Junior_Guide.docx): Complete technical guide in Microsoft Word format with tables, callout notes, and line-by-line explanations.
* [**`Agent_Prompt.md`**](file:///C:/Kuliah/Semester%203/Algodat/Stack/Agent_Prompt.md): Task specifications.

---

## 🚀 How to Run

### 1. Compile and Run the Java Code

```bash
javac Stack.java
java Stack
```

### 2. Generate the Word Guide (`.docx`)

```bash
pip install python-docx
python generate_guide.py
```

---

## 📋 Stack Operations

| Operation | What it Does | Complexity |
| :--- | :--- | :---: |
| `push(value)` | Adds a number to the top | $\mathcal{O}(1)$ |
| `pop()` | Removes and returns the top number | $\mathcal{O}(1)$ |
| `peek()` | Views the top number without removing it | $\mathcal{O}(1)$ |
| `isEmpty()` | Checks if stack is empty (`top == -1`) | $\mathcal{O}(1)$ |
| `isFull()` | Checks if stack is full (`top == capacity - 1`) | $\mathcal{O}(1)$ |
| `size()` | Returns current number of elements (`top + 1`) | $\mathcal{O}(1)$ |
| `printStack()` | Prints all elements from top to bottom | $\mathcal{O}(n)$ |

---

## 💡 Quick Rules to Remember

1. **`top` starts at `-1`**: Since array indexing starts at `0`, an empty stack is represented by `-1`.
2. **Push**: Always check `isFull()` before incrementing `top`.
3. **Pop**: Always check `isEmpty()` before accessing `arr[top]` and decrementing `top`.
