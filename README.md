# Tugas 2 - PBP
## I'd like to welcome you to Etrean Luminant Store (¬‿¬)

> [!NOTE]
> A Model-View-Template for an E-Commerce application 

Website Tugas 2: [click here](http://figo-favian-pbptugas2figo.pbp.cs.ui.ac.id/)

### 🟦🟥 Step-by-step:
1. Membuat Proyek Django baru
  - Membuat folder, directory, dan repo baru
  - Di dalam folder, gunakan `python -m venv venv` untuk membbuat virtual environment yang baru kemudian jalankan
  - Menyiapkan Framework dengan menginstall Django. Jika perlu, install dependencies lainnya dalam `requirements.txt`

  - Setelah semua sudah disiapkan, jalankan `python manage.py startproject [nama project] .` untuk membbuat proyek baru
2.  Buatlah aplikasi dengan menjalankan `python manage.py startapp main`
  -  Dalam `settings.py`, tambahkan `'main'`. Implementasi:
    ```
    INSTALLED_APPS = [
    'main',
     ...
     ]
    ```

3. Melakukan routing
  - Dengan `django.urls` import `path` dan `include` dalam urls.py

4. Membuat model pada aplikasi main 
  - Dalam `models.py` di directory main, import `models`
  - Buat class dengan nama `Product` dengan tiga attribut yaitu `name, price, dan description.`
  ```
  class Product(models.Model):
    mood = models.CharField(max_length=100) # nama produk disini
    price = models.IntegerField()  # harga produk
    description = models.TextField()  # deskripsi produk
  ````
  - Buatlah migrasi mode dengan menjalankan `python manage.py makemigrations`
  - Kemudian eksekusikan migrasi dengan `python manage.py migrate`

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi, nama, dan kelas
  - isi views.py:
  ```
from django.shortcuts import render

def ingfo(request):
    context = {
        'nama': 'Figo Favian Ragazo',  # nama
        'kelas': 'PBP F'  # kelas 
    }
    return render(request, 'main.html', context)
  ``` 
  - Buat folder baru bernama di dalam main bernama `templates`
  - Dalam folder tersebut, buatlah file `main.html`
  - Isi main.html:
```
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Info</title>
</head>
<body>
    <h1>Etrean Luminant Store</h1>
    <p>Nama: {{ nama }}</p>
    <p>Kelas: {{ kelas }}</p>
</body>
</html>
```
  -
  
6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
  - Buatlah file baru dengan nama `urls.py` dalam main
  - Isi urls.py:
```
from django.urls import path
from main.views import ingfo 
app_name = 'main'
urlpatterns = [
    # bisa menambahkan URL utk views
    path('', ingfo, name='main')
]
```

7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
   - push repository lokal ke PWS 


### 🟦🟥 Bagan 

Visualisasi:

![image](https://github.com/user-attachments/assets/2f8c7cf5-e6a5-4ef3-a54c-3a313b13330b)

[Source Img](https://nitinnain.com/djangos-request-response-cycle/)

> Penjelasan Hubungan Komponen:

`urls.py`: Bertugas mencocokkan URL yang dikirimkan klien dengan view yang sesuai. Misalnya, jika klien mengirimkan request ke /home/, urls.py akan memetakan request tersebut ke view yang menangani halaman home.

`views.py`: Bertanggung jawab untuk menangani logika dari request, termasuk pengambilan data dari model dan menyiapkan data untuk template. Jika data dari database diperlukan, `views.py` akan memanggil `models.py`

`models.py`: Berisi definisi model dan struktur data. Menggunakan Django ORM, model mengatur interaksi dengan database. Misalnya, jika sebuah view memerlukan daftar item dari database, `models.py` akan menyediakan akses ke data tersebut.

`HTML Template`: Setelah data dikumpulkan di view, template digunakan untuk merender data tersebut menjadi halaman web yang akan ditampilkan kepada klien.

`Client Response`: Setelah halaman HTML selesai dirender, Django akan mengembalikannya sebagai respons HTTP ke klien, yang kemudian akan ditampilkan di browser atau perangkat lunak klien.

### 🟦🟥 Fungsi Git 
Fungsi Git dalam pengembangan perangkat lunak: Git adalah alat kontrol versi yang memfasilitasi pelacakan perubahan kode secara efektif dan kolaboratif. Dengan fitur branching dan merging, Git memungkinkan pengembangan beberapa fitur secara paralel tanpa mengganggu kode utama. Git juga menyimpan riwayat perubahan, memungkinkan rollback jika terjadi kesalahan, dan menjaga integritas proyek. Integrasi dengan platform seperti GitHub mendukung kolaborasi tim secara online, menjadikan pengembangan perangkat lunak lebih terstruktur, aman, dan efisien.

### 🟦🟥 Framework Django sebagai permulaan pembelajaran pengembangan perangkat lunak
Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak: Django dipilih sebagai langkah awal dalam belajar pengembangan perangkat lunak karena memiliki arsitektur yang jelas dan fitur bawaan yang kaya seperti autentikasi dan panel admin. Ini mengurangi beban teknis sehingga pemula bisa fokus pada logika aplikasi. Dokumentasinya yang lengkap, komunitas yang aktif, serta integrasi keamanan membuat Django sangat ramah bagi pemula dan memberikan pondasi yang kuat untuk pengembangan proyek yang lebih besar.

### 🟦🟥 Model pada Django sebagai ORM
Mengapa model pada Django disebut sebagai ORM (Object-Relational Mapping): Django menggunakan ORM untuk memetakan objek dalam kode Python ke tabel di basis data relasional. Dengan ORM, pengembang dapat berinteraksi dengan data menggunakan metode Python tanpa perlu menulis SQL langsung. Setiap class model merepresentasikan tabel, dan setiap atributnya adalah kolom dalam tabel, yang membuat pengelolaan dan manipulasi data lebih mudah dan intuitif.

# Tugas 3 - PBP

## QnA:
### 🟦🟥 Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam pengembangan sebuah platform, pertukaran data antara berbagai komponen sistem baik itu frontend, backend, maupun eksternal merupakan hal yang penting untuk diimplementasikan. Maka dari itu, data delivery dibutuhkan. Sebagai contoh, data delivery biasanya menggunakan protokol seperti HTTP dan data sering kali dikirim dalam format seperti JSON atau XML.

### 🟦🟥 Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer dikarenakan syntax yang lebih sederhana atau mudah dibaca dan dalam pengembagan web, JSON juga lebih ringan dan lebih cepat untuk diproses. Selain itu, JSON juga lebih lebih praktis dan efisien dalam pengiriman data.

### 🟦🟥 Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Pada form Django, fungsi dari method `is_valid` bertujuan untuk memvalidasi data yang dikirimkan oleh pengguna sebelum diproses ke dalam database. Validasi ini mencegah terjadinya kesalahan pada penyimpanan atau pengolahan data seperti tipe data yang salah atau field yang kosong. Jika data invalid, method akan mengembalikan nilai `False`, dan sebaliknya method ini mengembalikan nilai `True` jika data valid.

### 🟦🟥 Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Sebelumnya, CSRF adalah serangan di mana penyerang mencoba membuat permintaan ke server dengan menggunakan kredensial pengguna yang sedang login tanpa sepengetahuan. Dengan menggunakan token CSRF, Django memastikan setiap permintaan POST yang dilakukan berasal dari sumber yang sah yang dibuat oleh aplikasi itu sendiri. Token CSRF memiliki nilai yang unik yang kemudian server akan memverifikasi token tersebut saat menerima permintaan. Jika dibiarkan tanpa `csrf_token`, penyerang dapat mengirimkan permintaan tanpa izin pengguna, mengubah data, dan hal berbahaya lainnya. 

### 🟦🟥 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?
1. Untuk membuat input form untuk objek model, saya terlebih dahulu membuat skeleton berupa kerangka views. Guna melakukan ini sebelum melakukan tahap selanjutnya adalah supaya desain dalam situs web konsisten dan juga mencegah adanya pengulangan kode yang sama.
   Langkah implementasi: Pada direktori utama, inisiasi direktori baru bernama `templates` dan sisipkanlah HTML bernama `base.html` didalamnya (sebagai template dasar). Kemudian, saya menambahkan 'DIRS': [BASE_DIR / 'templates'] dalam settings.py agar `base.html` terbaca 

2. Untuk memperkuat keamanan dalam kode, saya mengubah primary key dari Integer menjadi UUID
   Langkah Implementasi: Hapus `db.sqlite3`, ubah `models.py` dengan import uuid dan tambahkan implementasi yang sesuai, kemudian migrate. 

3. Setelah sudah melakukan setup setup pada langkah selanjutnya, saya mengimplementasi input form. Tujuannya adalah agar saya dapat menambahkan data baru dalam halaman utama (dalam kasus ini, yaitu data Product)
   Langkah implementasi: Dalam direktori `main/`, buatlah `forms.py` kemudian saya menyesuaikan method untuk pembuatan forms. Selanjutnya, saya merevisi `views.py` dengan mengimport beberapa hal dan membuat function baru sebagai penerima request, import method `create_product`

4. Untuk memastikan apakah sudah berhasil, saya menjalankan manage.py dan kemudian membuka http://localhost:8000 

5. Langkah selanjutnya yang saya terapkan adalah dengan membuat 4 fungsi dalam `views.py` berupa XML, JSON, XML by ID, dan JSON by ID sebagai formatnya. Keempat fungsi ini berfungsi untuk memperlihatkan data data baru yang sudah ditambahkan.
   Langkah Implementasi: Membuat masing masing fungsi di dalam `views.py`, kemudian import dan inisiasi path masing masing method di dalam `urls.py`. 
Untuk memeriksa keempat format, saya menggunakan http://localhost:8000/xml/ , http://localhost:8000/json/ , http://localhost:8000/xml/[id]/ , dan http://localhost:8000/json/[id]/ 
Sebagai contoh:
{
    "model": "main.product",
    "pk": "c7af16dd-0ded-4915-b104-cc0cf0b172d8",
    "fields": {
      "name": "Iphone Galaxy Tab",
      "price": 399,
      "description": "Iphone x Android collabb cuyy"
    }
  }
Maka id-nya berupa  "pk": "c7af16dd-0ded-4915-b104-cc0cf0b172d8"

### 🟦🟥 Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
![image](https://github.com/user-attachments/assets/64c95725-cbc1-49ae-9ba3-771ae9e92a24)
![image](https://github.com/user-attachments/assets/01da1508-8250-4700-b8ca-63d9a55104bf)
![image](https://github.com/user-attachments/assets/bb742c2c-aad9-4279-985e-fc926c1e00f6)
![image](https://github.com/user-attachments/assets/343c602d-06f2-47c4-b92f-e4bca102a12d)



