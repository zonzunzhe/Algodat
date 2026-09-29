class Burung extends Entity {
    public Burung(Object nilai) {
        super(nilai);
    }

    public void terbang() {
        System.out.println("Burung [" + this.nilai + "] terbang.");
    }
}

class Mobil extends Entity {
    public Mobil(Object nilai) {
        super(nilai);
    }

    public void berenang() {
        System.out.println("Mobil [" + this.nilai + "] berenang.");
    }
}

public class Main {
    public static void main(String[] args) {
        LinkedList rantai = new LinkedList();

        rantai.tambah(new Burung("Elang"));
        rantai.tambah(new Mobil("Amfibi"));
        rantai.tambah(new Burung(99));

        rantai.cetak(); 
    }
}