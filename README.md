# Belajar Algoritma dan Struktur Data

Repositori ini berisi kumpulan latihan dan implementasi dasar struktur data serta algoritma menggunakan bahasa Java. Dibuat sebagai catatan belajar mandiri untuk memahami bagaimana data dikelola dan diproses di dalam program.

---

## Apa itu Struktur Data?

Secara sederhana, **struktur data** adalah cara kita mengatur, menyusun, dan menyimpan data di dalam memori komputer agar bisa digunakan secara efisien.

Bayangkan seperti merapikan barang:
* Jika barang ditaruh sembarangan, kita butuh waktu lama untuk mencarinya.
* Jika disimpan di rak berlabel atau kotak khusus, kita bisa mengambil atau menambah barang dengan cepat dan teratur.

### Struktur Data Dasar yang Dipelajari:
1. **Array**: Kumpulan data berurutan dengan ukuran tetap.
2. **Linked List**: Data yang saling terhubung seperti gerbong kereta melalui penunjuk (*pointer/reference*).
3. **Stack (Tumpukan)**: Konsep tumpukan piring (*LIFO - Last In, First Out*). Data yang terakhir masuk akan pertama kali diambil.
4. **Queue (Antrean)**: Konsep antrean tiket (*FIFO - First In, First Out*). Data yang pertama masuk akan pertama kali diproses.
5. **Tree**: Struktur data hierarkis bercabang seperti silsilah keluarga.



## Cara Menjalankan Program

Pastikan Java Development Kit (JDK) sudah terpasang di komputer Anda.

1. Buka terminal atau Command Prompt pada folder proyek.
2. Kompilasi file Java yang ingin dijalankan:
   ```bash
   javac Main.java
   ```
3. Jalankan program:
   ```bash
   java Main
   ```

### Tingkat Efisiensi Big-O (Terbaik ke Terburuk)

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)$$

* **$O(1)$ (Konstan):** Luar biasa. Waktu eksekusi tidak terpengaruh oleh ukuran data.
* **$O(\log n)$ (Logaritmik):** Sangat baik. Penambahan data hanya berdampak sangat kecil pada waktu proses.
* **$O(n)$ (Linear):** Adil. Waktu eksekusi sebanding lurus dengan jumlah data.
* **$O(n \log n)$ (Linearitmik):** Cukup baik. Standar efisiensi untuk algoritma pengurutan optimal.
* **$O(n^2)$ (Kuadratik):** Buruk. Waktu melonjak drastis saat data membesar (biasanya akibat nested loop).
* **$O(2^n)$ & $O(n!)$ (Eksponensial & Faktorial):** Sangat buruk. Cepat membuat program kehabisan memori atau waktu (*hang*).

---

### Operasi Struktur Data

| Struktur Data | Akses (Rata-rata) | Pencarian (Rata-rata) | Penambahan (Rata-rata) | Penghapusan (Rata-rata) | Kasus Terburuk (Worst) |
| --- | --- | --- | --- | --- | --- |
| **Array** | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ | $O(n)$ |
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ *(di awal)* | $O(1)$ *(di awal)* | $O(n)$ |
| **Doubly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ | $O(1)$ | $O(n)$ |
| **Stack** | $O(n)$ | $O(n)$ | $O(1)$ *(push)* | $O(1)$ *(pop)* | $O(n)$ |
| **Queue** | $O(n)$ | $O(n)$ | $O(1)$ *(enqueue)* | $O(1)$ *(dequeue)* | $O(n)$ |
| **Hash Table** | $O(1)$ | $O(1)$ | $O(1)$ | $O(1)$ | $O(n)$ *(tabrakan hash)* |
| **Binary Search Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ *(pohon miring)* |
| **AVL / Red-Black Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ |

---

### Algoritma Pengurutan (Sorting)

| Algoritma | Waktu Terbaik (*Best*) | Waktu Rata-rata (*Average*) | Kasus Terburuk (*Worst*) | Memori Tambahan (*Space*) |
| --- | --- | --- | --- | --- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ |
### Algoritma Pencarian (Searching)
| Algoritma | Kondisi Data | Kasus Terbaik (*Best*) | Rata-rata (*Average*) | Kasus Terburuk (*Worst*) |
---
### Kontribusi
Kontribusi berupa penambahan materi, optimalisasi kode, perbaikan bug, atau penambahan penjelasan sangat terbuka:

1. Fork repositori ini
2. Buat branch fitur baru
   ``` bash
   git checkout -b fitur/algoritma-baru
   ```
4. Lakukan commit perubahan
   ``` bash
   git commit -m 'feat: tambah implementasi'
   ```
6. Push ke branch
   ``` bash
   git push origin fitur/algoritma-baru
   ```
8. Buat sebuah Pull Request




| --- | --- | --- | --- | --- |
| **Linear Search** | Acak / Terurut | $O(1)$ | $O(n)$ | $O(n)$ |
| **Binary Search** | Harus Terurut | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
