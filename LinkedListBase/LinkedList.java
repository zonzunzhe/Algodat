class Node {
    Object data;
    Node next;

    public Node(Object data) {
        this.data = data;
        this.next = null;
    }
}

abstract class AbstractList {
    Node head;

    public abstract void insert(Object data);
    public abstract void tambah(Object data);
    public abstract void cetak();
}

public class LinkedList extends AbstractList {
    
    @Override
    public void insert(Object data) {
        Node nodeBaru = new Node(data);
        nodeBaru.next = head;
        head = nodeBaru;
    }

    @Override
    public void tambah(Object data) {
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

    @Override
    public void cetak() {
        Node sementara = head;
        while (sementara != null) {
            System.out.print(sementara.data + " -> ");
            sementara = sementara.next;
        }
        System.out.println("null");
    }
}