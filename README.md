# Assignment 2: Model-View-Template (MVT) implementation in Django
Pada tugas kali ini, saya membuat suatu app e-commerce sederhana dengan ide menjual buku-buku bekas menggunakan Django.
* LINK: [http://sultan-ibnu-prelovedbooks.pbp.cs.ui.ac.id/](http://sultan-ibnu-prelovedbooks.pbp.cs.ui.ac.id/)

## Checklist Tugas
-   [x] Membuat sebuah proyek Django baru.
-   [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
-   [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
-   [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    -   `name`
    -   `price`
    -   `description`
-   [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
-   [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
-   [x] Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
-   [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut.
### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial)!
* Pertama yang saya lakukan adalah mengaktifkan _virtual environment_ karena seperti yang saya telah pelajari di dalam kelas dan tutorial, _virtual environment_ berfungsi untuk mengisolasi _dependencies_ antar proyek yang berbeda sehingga tidak terjadi hal-hal yang tidak diinginkan.

'''env\Scripts\activate
'''

* Membuat project baru Django dengan perintah seperti di bawah untuk membuat struktur proyek Django baru di dalam direktori _pre-love-books_.

'''django-admin startproject pre_loved_books .
'''



