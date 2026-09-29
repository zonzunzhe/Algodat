public class Entity {
    Object nilai;

    public Entity(Object nilai) {
        this.nilai = nilai;
    }

    @Override
    public String toString() {
        return String.valueOf(this.nilai);
    }
}
