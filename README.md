# Tugas 2 - PBP
## I'd like to welcome you to Etrean Luminant Store (¬‿¬)

> [!NOTE]
> A Model-View-Template for an E-Commerce application 

Website Tugas 2: [click here](http://figo-favian-pbptugas2figo.pbp.cs.ui.ac.id/)

### Step-by-step:
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


### Bagan 

Visualisasi:
![image](https://github.com/user-attachments/assets/2f8c7cf5-e6a5-4ef3-a54c-3a313b13330b)
[Source Img](https://nitinnain.com/djangos-request-response-cycle/)

Client Request 
      |
      v
   urls.py -- Cek pola URL dan route ke view yang sesuai --> views.py
      |                                                    |
      |                                                    v
      |                 Interaksi dengan models.py untuk mengambil  data jika diperlukan
      v                                  
  models.py -- Kirim data yang diambil dari database ke views.py
      |
      v
HTML Template -- Render data menjadi halaman HTML
      |
      v
Client Response -- Kirim halaman HTML ke client

> Penjelasan Hubungan Komponen:
`urls.py`: Bertugas mencocokkan URL yang dikirimkan klien dengan view yang sesuai. Misalnya, jika klien mengirimkan request ke /home/, urls.py akan memetakan request tersebut ke view yang menangani halaman home.

`views.py`: Bertanggung jawab untuk menangani logika dari request, termasuk pengambilan data dari model dan menyiapkan data untuk template. Jika data dari database diperlukan, `views.py` akan memanggil `models.py`

`models.py`: Berisi definisi model dan struktur data. Menggunakan Django ORM, model mengatur interaksi dengan database. Misalnya, jika sebuah view memerlukan daftar item dari database, `models.py` akan menyediakan akses ke data tersebut.

`HTML Template`: Setelah data dikumpulkan di view, template digunakan untuk merender data tersebut menjadi halaman web yang akan ditampilkan kepada klien.

`Client Response`: Setelah halaman HTML selesai dirender, Django akan mengembalikannya sebagai respons HTTP ke klien, yang kemudian akan ditampilkan di browser atau perangkat lunak klien.
