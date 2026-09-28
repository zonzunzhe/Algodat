class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList {
    Node head;

    public void tambah(int data) {
        Node nodeBaru = new Node(data);

        if (head == null) {
            head = nodeBaru;
            return;
        }

        Node sementara = head;
        while (sementara.next != null) {
            sementara = sementara.next;
        }

        sementara.next = nodeBaru;
    }

    public void insert(int data) {
        Node nodeBaru = new Node(data);
        nodeBaru.next = head;
        head = nodeBaru;
    }

    public void delete(int data) {
        if (head == null) {
            return;
        }

        if (head.data == data) {
            head = head.next;
            return;
        }

        Node sementara = head;
        while (sementara.next != null && sementara.next.data != data) {
            sementara = sementara.next;
        }

        if (sementara.next != null) {
            sementara.next = sementara.next.next;
        }
    }

    public void cetak() {
        Node sementara = head;
        while (sementara != null) {
            System.out.print(sementara.data + " -> ");
            sementara = sementara.next;
        }
        System.out.println("null");
    }
}