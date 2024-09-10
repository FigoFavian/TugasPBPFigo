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
