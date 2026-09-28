public class Main {
    public static void main(String[] args) {
        LinkedList rantaiData = new LinkedList();

        rantaiData.tambah(10);
        rantaiData.tambah(20);
        rantaiData.tambah(30);

        rantaiData.cetak();

        rantaiData.insert(5);
        rantaiData.cetak();

        rantaiData.delete(20);
        rantaiData.cetak();
    }
}