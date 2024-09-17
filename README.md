# Platform Based Programming Individual Assignment

| NAME             | ID                                         | PBP CLASS  |
|-----------------|------------------------------------------------|--------|
| Sultan Ibnu Mansiz | 2306275840 | D |

Pada tugas ini, saya membuat suatu projek e-commerce sederhana bernama "Second Chapters <3" dengan ide menjual buku-buku bekas. Saya menggunakan konsep _Model-View-Template_ (MVT) pada Django untuk membangun projek ini.

- LINK: [Second Chapters <3](http://sultan-ibnu-prelovedbooks.pbp.cs.ui.ac.id/)


# Assignment 3: Implementation of Forms and Data Delivery in Django
## Checklist Tugas

- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML _by_ ID, dan JSON _by_ ID.
- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada _root_ folder.

### Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Implementasi sebuah platform memiliki komponen-komponen yang punya fungsi masing-masing. Semua data yang diberikan, disimpan, dan ditampilkan sangat berkaitan erat dengan salah satu komponennya yaitu database. Data-data tersebut harus segera digunakan ketika ada user yang mengakses atau me _request_ suatu data. Di situlah peran penting dari _data delivery_ yaitu agar data-data yang dikelola bisa diakses di waktu dan tempat yang tepat. _Data delivery_ juga sangat berfungsi agar data dapat dikirim dari satu komponen ke komponen lainnya.


### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik daripada XML karena beberapa alasan. Pertama, JSON lebih ringkas dibandingkan XML karena menggunakan lebih sedikit karakter untuk merepresentasikan data yang sama, sehingga menghemat ruang dan mempermudah transfer data. Selain itu, JSON juga lebih mudah di-parse oleh bahasa pemrograman modern, yang menjadikannya lebih efisien dalam proses pengolahan data. Terakhir, struktur JSON yang sederhana membuatnya lebih mudah dibaca dan dipahami oleh manusia, sehingga mempermudah pengembang untuk bekerja dengan data tersebut.

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada Django berfungsi untuk mengecek apakah data yang dimasukkan oleh user ke dalam form merupakan data yang sesuai (tipe data atau apakah form wajib diisi). Pada projek ini, `is_valid()` akan mengecek apa yang sudah ditentukan di dalam `ProductForm` yang mengarah ke `models`

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita memerlukan `csrf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan _Cross-Site Request Forgery_ (CSRF). Tanpa `csrf_token`, penyerang bisa mengirimkan permintaan palsu dengan memanfaatkan session yang sudah ada di browser user/client, sehingga membuat aplikasi rentan terhadap serangan CSRF.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

* Pertama saya membuat file baru bernama `forms.py` yang saya letakkan di direktori `main` lalu saya memasukkan kode seperti di bawah

    ```python
        from django.forms import ModelForm
        from main.models import Product

        class ProductForm(ModelForm):
            class Meta:
                model = Product
                fields = ["name", "author", "price", "description"]
    ```

* Selanjutnya saya menambah impot _redirect_ ke file `views.py`

    ```python
        from django.shortcuts import render, redirect
    ```
    Masih di file yang sama, saya mebuat class _function_ bernama `create_product()` yang berfungsi untuk menangani penambahan buku oleh user. _redirect_ yang diimpor sebelumnya digunakan di function ini untuk mengarahkan ke halaman yang dituju.

    ```python
        def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```

* Pada file `views.py` di fungsi `show_main`, saya menambahkan variabel _product_ yang sebelumnya mengarah ke `models` dan akan menuju `templates` untuk ditampilkan.

    ```python
        product = Product.objects.all()

        context = {
            'student_name': 'Sultan Ibnu Mansiz',
            'student_id': 2306275840,
            'student_class': 'PBP D',  
            'description': 'Kami adalah destinasi utama bagi para pencinta buku yang mencari harta karun literatur dengan harga terjangkau. Di sini, setiap buku memiliki cerita yang kaya dan penuh kenangan. Toko kami berkomitmen untuk memberikan kesempatan kedua bagi buku-buku yang sudah melewati perjalanan hidupnya, agar tetap dapat dinikmati oleh pembaca baru.',
            'greet': 'Selamat berbelanja',
            'products': product,
        }
    ```
    Saya juga menambahkan beberapa variabel baru yang nanti akan ditampilkan di `templates`.

* Pada file `urls.py` yang berada di direktori `main`, saya mengimpor fungsi `create_product`
  di dalam _urlpatterns_ saya menambahkan URL untuk mengakses fungsi yang sebelumnya diimpor

    ```python
        urlpatterns = [
        ...
        path('create-product', create_product, name='create_product'),
        ]
    ```

* Membuat berkas HTML baru bernama `create_product` di dalam direktori `main/templates`. Lalu, file tersebut saya isi dengan kode di bawah

    ```html
        {% extends 'base.html' %}

        {% block content %}
        <h1>Tambahkan buku</h1>

        <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td>
                <input type="submit" value="Masukkan" />
            </td>
            </tr>
        </table>
        </form>

        {% endblock %}
    ```

* Saya menambahkan beberapa baris kode di `main.html` yang dibungkus di dalam `{% block content %}` 

    ```html
        <div id="center">
            {% if not products %}

            <p>Yahh.. Belum ada buku yang lagi dijual nih</p>
            {% else %}
            <table>
                <tr>
                <th>Name</th>
                <th>Author</th>
                <th>Price</th>
                <th>Description</th>
                </tr>

                {% comment %} Berikut cara memperlihatkan data buku di bawah baris ini
                {%endcomment %} 
                {% for product in products %}
                <tr>
                <td>{{product.name}}</td>
                <td>{{product.author}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                </tr>
                {% endfor %}
            </table>
            {% endif %}

            <br />

            <a href="{% url 'main:create_product' %}">
                <button>Tambahkan buku</button>
            </a>

            <form action="{% url 'main:clear_table' %}" method="post">
                {% csrf_token %}
                <button type="submit">Kosongkan tabel</button>
            </form>

            <br />
            <br />

            <p>
                © 2024 {{ student_name }} ({{ student_id }}, {{ student_class }}) — All
                Rights Reserved.
            </p>
            </div>
        </body>
        </html>
        {% endblock content %}
    ```
    Saya juga menambahkan data diri saya dan juga sebuah button untuk menghapus isi dari tabel.

* Saya menambahkan fungsi `clear_table()` pada file `views.py` agar bisa menghapus data yang ada di tabel HTML

    ```python
        def clear_table(request):
            Product.objects.all().delete()
            return redirect('main:show_main')
    ```

* Selanjutnya, sepertinya yang diminta, saya menambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML _by_ ID, dan JSON _by_ ID.

    ```python
        def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

* Setelah itu, saya membuat routing URL untuk masing-masing `views` yang telah ditambahkan sebelumnya.

    ```python
        urlpatterns = [
        ...
        path('xml/', show_xml, name='show_xml'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/', show_json, name='show_json'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
    ```

- [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat _screenshot_ dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.

* `/xml/`
    ![/xml/](resources/postman_xml.png)

* `/xml/[id]`
    ![/xml/[id]](resources/postman_xmlid.png)

* `/json/`
    ![/json/](resources/postman_json.png)

* `/json/[id]`
    ![/json/[id]](resources/postman_jsonid.png)

- [x] Melakukan `add`-`commit`-`push` ke GitHub.


# Assignment 2: Model-View-Template (MVT) implementation in Django
## Checklist Tugas

- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
- [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
  - `name`
  - `price`
  - `description`
- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [x] Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial)!

- Pertama yang saya lakukan adalah mengaktifkan _virtual environment_ karena seperti yang saya telah pelajari di dalam kelas dan tutorial, _virtual environment_ berfungsi untuk mengisolasi _dependencies_ antar proyek yang berbeda sehingga tidak terjadi hal-hal yang tidak diinginkan.

- Membuat project baru Django dengan perintah `django-admin startproject pre_loved_books .`

- Membuat aplikasi bernama `main` dengan perintah `python manage.py startapp main`. Lalu, daftarkan aplikasi `main` tersebut ke dalam file settings.py di dalam direktori pre_loved_books.

    ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main', # <------
    ]
    ```

- Membuat file bernama `urls.py` di dalam direktori main yang telah kita buat sebelumnya. Lalu, isi file tersebut dengan

    ```python
	from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

* Saya membuat model pada aplikasi main sesuai ketentuan dan menambahkan satu buah atribut dengan code

    ```python
	from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255)
        author = models.CharField(max_length=255, default='')
        price = models.DecimalField(decimal_places=2, max_digits=15)
        description = models.TextField()

        @property
        def is_book_expensive(self):
            return self.price > 50000
    ```

* Setelah itu, Di dalam file `views.py` pada aplikasi main saya menambahkan code
    ```python
	from django.shortcuts import render

    def show_main(request):
        context = {
            'name' : 'Norwegian Wood',
            'author': 'Haruki Murakami',
            'price': 100000,
            'description': 'Edisi ini menggunakan bahasa Inggris karena merupakan barang impor. Hanya dibaca oleh diri sendiri dan selalu tersimpan rapih. Tidak ada kerusakan apapun kecuali kertasnya yang mulai menguning.'
        }

        return render(request, "main.html", context)
    ```
  yang nantinya akan menampilkan value sesuai keys di file ini pada file HTML.

* Kemudian, saya menambahkan _routing_ di `urls.py` dalam aplikasi `main` untuk mengatur _path_ yang menghubungkan fungsi yang sudah ada di `views.py`.
    ```python
	from django.contrib import admin
    from django.urls import path,  include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

* Terakhir, saya menghubungkan repositori saya dengan link yang mengarahkan ke pws lalu melakukan _deployment_ proyek yang telah saya buat agar bisa diakses di internet.

### Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![Diagram](resources/diagrams.png)
Diagram alur dimulai dari adanya client yang mengirim request di internet atau browsernya. Request itu diarahkan oleh `urls.py` dengan cara memetakan URL yang diminta ke `views.py`. `views.py` lalu memproses request tersebut yang juga dilanjutkan ke `models.py` jika ada data yang perlu disimpan atau diambil dari `database`. Setelah semua sudah terpenuhi, request dari client tadi akan ditampilkan lewat `HTML` yang telah dibuat.

### Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
Dari apa yang telah saya pelajari dan pahami, git sangat berguna khususnya dalam pengembangan perangkat lunak. Git berfungsi sebagai sistem kontrol yang sangat sistematis dan terkoordinasi dalam pengembangan perangkat lunak. Hal itu memudahkan para developer untuk melihat perubahan atau penambahan apa saja yang terjadi, berkolaborasi, menyimpan riwayat kode, dan penggabungan kontribusi dari banyak developer. 

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Beberapa alasan menurut pengalaman saya sejuah ini adalah karena Django menyediakan banyak fitur bawaan yang sangat memudahkan pemula bisa lebih fokus memahami bagaimana cara kerja pengembangan perangkat lunak dibandingkan mempelajari code yang rumit. Selain itu, menurut saya, Django memiliki struktur proyek yang rapih dan sistematis sehingga dapat belajar bagaiman cara mengorganisasi code dengan baik.

### Mengapa model pada Django disebut sebagai ORM?
ORM adalah alat yang menerjemahkan kode Python menjadi `SQL`. Di Django, kita hanya perlu mendefinisikan model dan atributnya menggunakan Python, lalu model tersebut akan diubah menjadi `SQL` melalui proses migrasi dan disimpan di folder migrations.
