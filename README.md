# Tugas PBP
## I'd like to welcome you to Etrean Luminant Store (¬‿¬)

> [!NOTE]
> A Model-View-Template for an E-Commerce application 

Website Tugas: [click here](http://figo-favian-pbptugas2figo.pbp.cs.ui.ac.id/)

<details>
  <summary>Tugas 2</summary>

## Tugas 2 💻 

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
</details>

<details>
  <summary>Tugas 3</summary>

## Tugas 3 💻 

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

</details>

<details>
  <summary>Tugas 4</summary>

## Tugas 4 💻 

### 🟦🟥 Apa perbedaan antara HttpResponseRedirect() dan redirect()

Secara umum, redirect() lebih fleksibel sebab HttpResponseRedirect() hanya hanya menerima URL sebagai argumen, redirect() mampu menerima model, view, atau URL dan menyederhanakan pengalihan dengan menyelesaikan URL menggunakan fungsi reverse() secara otomatis. 

```python
Contoh HttpResponseRedirect(): `return return HttpResponseRedirect('/main/')`
Contoh redirect(): `return redirect('main:show_main')`
```

### 🟦🟥 Jelaskan cara kerja penghubungan model Product dengan User!

Penghubungan model Product dengan User dilakukan melalui `ForeignKey` yang menghasilkan relasi one-to-many. Relasi one-to-many memastikan bahwa setiap produk dimiliki oleh satu pengguna, namun pengguna tersebut bisa memiliki banyak produk. Dalam implementasi, produk yang dibuat oleh user akan secara otomatis terhubung dengan user yang sedang login menggunakan `request.user`. Jika pengguna dihapus, semua produk yang terkait juga akan ikut dihapus. Relasi ForeignKey menggunakan parameter on_delete=models.CASCADE, yang berarti bahwa jika pengguna (User) dihapus, maka semua produk yang terkait dengan pengguna tersebut juga akan ikut dihapus dari database. Ini membantu menjaga konsistensi data dan mencegah adanya produk yang "terputus" dari pengguna.
Berikut contohnya:

```python
class Product(models.Model): 
user = models.ForeignKey(User, on_delete=models.CASCADE) 
Id models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
name = models.CharField(max_length=100) 
price = models.IntegerField()
description = models.TextField()  
```

### 🟦🟥 Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses verifikasi identitas user. Tujuan dari autentikasi adalah memastikan bahwa pengguna benar-benar merupakan orang yang mereka klaim. Authorization adalah proses yang menentukan hak akses yang dimiliki pengguna setelah authentication berhasil. Authorization memastikan apakah pengguna memiliki izin untuk mengakses sumber daya atau melakukan tindakan tertentu. Saat proses login, Django akan mengautentikasi melalui username dan password seperti umumnya, jika berhasil maka kemudian user akan diotorisasi. Berikut merupakan contoh implementasi dalam django:

```python
def login_user(request): 

if request.method == 'POST': 
form = AuthenticationForm(data=request.POST)

 if form.is_valid(): 
user = form.get_user()
login(request, user) 
response = HttpResponseRedirect(reverse("main:ingfo")) 
response.set_cookie('last_login', str(datetime.datetime.now())) 
return response
else:
 form = AuthenticationForm(request) 
context = {'form': form} 
return render(request, 'login.html', context)
```

### 🟦🟥 Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan sessions dan cookies. Saat user berhasil login, Django akan membuat session di server yang menyimpan informasi pengguna, seperti ID pengguna dan status autentikasi. Django kemudian mengirimkan session ID ke browser klien dalam bentuk cookie. Setiap kali pengguna melakukan request ke server, browser akan mengirim kembali cookie yang berisi session ID tersebut. Django kemudian membaca session ID tersebut, mencocokkannya dengan informasi sesi yang tersimpan di server, dan melanjutkan interaksi tanpa perlu pengguna login kembali.

Cookies memiliki kegunaan lain seperti menyimpan preferensi pengguna(bahasa yang dipilih, tema tampilan),  menyimpan status login user, melacak aktifitas user di seluruh situs, dan lain lain. Django mengimplementasikan beberapa sistem keamanan kepada cookies seperti CSRF Protection, Secure Cookies, dan HttpOnly, sebab terdapat cookies yang tidak sepenuhnya aman. 

### 🟦🟥 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

✅ Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

1) Mengimplementasikan fungsi register dalam `views.py` dengan method `register`

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

```

Penjelasan:
> Membuat form pendaftaran melalui `UserCreateForm()` nya Django. Dengan menangani POST, Jika form sudah valid maka data akan disimpan. Kemudian setelah terdaftar, akan di redirect ke halaman login

2) Mengimplementasikan fungsi login dalam `views.py` dengan method `login_user`

```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:ingfo"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

Penjelasan:
> method ini menggunakan beberapa fungsi dari Django seperti AuthenticationForm untuk login, kemudian jika berhasil `HttpResponseRedirect` akan meredirect ke halaman utama.

3) Mengimplementasikan fungsi  dalam `views.py` dengan method `logout_user`

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

> Penjelasan:
* logout() akan menghapus session user dan setelah itu cookie akan di delete

4) Memetakan masing masing method ke dalam `urls.py`:

```python
urlpatterns = [
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```

5) Menambahkan `@login_required(login_url='/login')` di `views.py` untuk pengguna yang ingin login.


✅ Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

1) Berikut dua akun pengguna yang diregister:

![Screenshot 2024-09-25 082118](https://github.com/user-attachments/assets/6fc9ca28-9ca7-4e31-980e-db67c430c9d8)

![Screenshot 2024-09-25 082234](https://github.com/user-attachments/assets/e717dc92-90e8-4f93-bd4e-9e3c765afa29)


2) Login kedua user dan tambahkan masing masing tiga dummy:

![Screenshot 2024-09-25 083216](https://github.com/user-attachments/assets/5e2513f9-d82f-4f88-948d-2612fd3f92ae)

![Screenshot 2024-09-25 083500](https://github.com/user-attachments/assets/ba59cc07-c53b-48d0-9c4c-321a3f6ac23e)


✅ Menghubungkan model Product dengan `User`

Mengupdate method `Product` di `models.py`

```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100) 
    price = models.IntegerField()  
    description = models.TextField()  
```


> Penjelasan: Menambahkan field user dengan value `models.ForeignKey`. Penambahan ini akan menghubungkan User dengan Product dan akan berguna agar user dapat memiliki banyak Product. 


✅ Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

1) Membuat cookie dengan nama `last_login` berisi waktu dari user login saat user tersebut berhasil login

```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:ingfo"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

2) Menampilkan username sesuai data dengan menggunakan `request.user.username`:

```python
@login_required(login_url='/login')
def ingfo(request):
    product_entries = Product.objects.filter(user=request.user)
    
    context = {
        'nama': request.user.username,  # nama
        'kelas': 'PBP F',  # kelas 
        'product_entries': product_entries,
        'last_login': request.COOKIES['last_login'],
        }
    
    return render(request, 'main.html', context)
```

3) Username dan waktu login ditampilkan di `main.html` dengan format `{{ }} `
```python
<p>Nama: {{ nama }}</p>
<h5>Sesi terakhir login: {{ last_login }}</h5>
 ```
</details>  

<details>
  
  <summary>Tugas 5</summary>

## Tugas 5 💻

### 🟦🟥 Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

1. Aturan !important
Jika ada aturan CSS yang menggunakan !important, aturan ini akan memiliki prioritas tertinggi dan menimpa semua aturan lainnya, terlepas dari urutan selector atau sumbernya.
html:
```python
<p id="text" class="text" style="color: blue;">Hello World</p>
```
css:
```python
p { color: red !important; }
```

2. Inline Styles
Inline CSS adalah gaya yang diterapkan langsung pada elemen HTML melalui atribut style. Ini memiliki prioritas lebih tinggi daripada selector ID, class, atau elemen dalam stylesheet eksternal atau internal.
Html:
```html
<p id="text" class="text" style="color: green;">Hello World</p>
```
Css:
```css
#text { color: yellow; }
```

3. Selector ID
Selector yang menggunakan ID (#id) memiliki prioritas lebih tinggi daripada class, pseudo-class, atau selector elemen. Jika elemen memiliki aturan yang ditentukan oleh ID, maka gaya ini akan diterapkan.
Html:
```html
<p id="text" class="text">Hello World</p>
```
Css:
```css
#text {
	color: blue;
}

.text {
	color: yellow;
}
```


4. Classes, Pseudo-classes, dan Attribute Selectors
Selector yang menggunakan class (.class), pseudo-class (:hover, :focus), atau attribute selector ([type="text"]) memiliki prioritas lebih tinggi daripada selector elemen (p, div), tetapi lebih rendah dari ID dan inline style.
html:
```html
<p class="text">Hello World</p>
```
Css:
```css
.text {
	color: red;
}

p {
	color: yellow;
}
```

5. Selector Elemen dan Pseudo-elemen
Selector elemen (seperti p, div, h1) memiliki prioritas paling rendah dibandingkan selector lainnya, kecuali jika tidak ada aturan yang lebih spesifik.
html:
```html
<p>Hello World</p>
```
Css:
```css
p { color: green; }
```

6. Urutan Definisi dalam Stylesheet
Jika terdapat dua aturan dengan prioritas yang sama (misalnya, dua aturan elemen atau dua aturan class), maka aturan yang didefinisikan terakhir dalam stylesheet akan diterapkan.
html
```html
<p>Hello World</p>
```
Css
```css
p { color: yellow; } p { color: blue; }
```

7. Urutan Sumber CSS
Inline CSS: Memiliki prioritas tertinggi di antara sumber-sumber CSS lainnya karena diterapkan langsung di elemen HTML.
Contoh: <div style="color: red;">Contoh</div>
Internal CSS: Ditulis dalam tag <style> di dalam halaman HTML dan memiliki prioritas lebih rendah dari inline CSS, tetapi lebih tinggi dari external CSS.
Html:
<style> div { color: green; } </style>

### 🟦🟥 Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design

Responsive design adalah pendekatan dalam desain web yang memungkinkan tampilan sebuah situs atau aplikasi untuk beradaptasi dengan berbagai ukuran layar, seperti desktop, tablet, dan smartphone. Semakin banyak pengguna yang mengakses internet melalui perangkat mobile. Dengan menggunakan responsive design, situs web dapat memberikan pengalaman pengguna (UX) yang lebih baik di semua perangkat tanpa memerlukan versi terpisah untuk desktop dan mobile.
Jika sebuah situs tidak responsif, pengguna perangkat mobile mungkin mengalami kesulitan, seperti elemen yang terlalu kecil, teks yang sulit dibaca, atau layout yang berantakan. Namun, situs dengan desain responsif akan menyesuaikan elemen seperti ukuran teks, gambar, dan tata letak sehingga tetap mudah diakses dan digunakan di layar yang lebih kecil.
Responsive design juga penting untuk Search Engine Optimization), karena mesin pencari seperti Google memberikan peringkat lebih tinggi pada situs yang mobile-friendly, sehingga meningkatkan visibilitas situs tersebut dalam hasil pencarian.
Contoh aplikasi yang sudah menerapkan responsive design adalah YouTube. Youtube menyesuaikan letak dan elemen-elemen agar dapat diakses dengan nyaman di desktop dan perangkat mobile. Sebaliknya, beberapa situs lama, termasuk situs pemerintahan atau sistem internal seperti SiakNG, mungkin belum menerapkan responsive design dengan baik. Saat diakses melalui perangkat mobile, tampilan situs-situs ini sering kali tidak proporsional, dengan elemen-elemen yang terlalu kecil atau rusak, sehingga pengguna perlu memperbesar layar untuk berinteraksi.

### 🟦🟥 Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Dalam CSS, margin, border, dan padding adalah bagian dari CSS Box Model, yang mengatur bagaimana ruang di sekitar elemen diatur. Berikut penjelasan perbedaan ketiganya serta cara mengimplementasikannya:
1. Margin adalah jarak di luar elemen yang memisahkannya dari elemen lain. Margin tidak memiliki warna atau garis dan berfungsi untuk menciptakan ruang kosong di sekitar elemen. Misalnya, jika ingin menambahkan margin 30px di semua sisi elemen, bisa digunakan kode berikut:

css:
```css
div { margin: 30px; }
```

2. Border adalah garis yang mengelilingi elemen, yang berada di antara margin dan padding. Border memiliki warna, ketebalan, dan gaya yang bisa diatur (misalnya solid, dashed, atau dotted). Setiap sisi border dapat dikustomisasi secara terpisah. Contoh implementasi border hitam dengan ketebalan 3px dan gaya solid adalah:
Css
```css
div { border: 3px solid black; }
```

3. Padding adalah jarak di dalam elemen, antara isi elemen dengan border. Padding menciptakan ruang di dalam elemen, menjauhkan konten dari tepi border. Padding juga bersifat transparan dan dapat diatur secara individual untuk setiap sisi (atas, bawah, kiri, kanan). Berikut contoh menambahkan padding 30px di semua sisi elemen:
Css:
```css
div { padding: 30px; }
```
### 🟦🟥 Jelaskan konsep flex box dan grid layout beserta kegunaannya!

#### Flexbox (Flexible Box Layout)

Flexbox adalah model layout satu dimensi yang digunakan untuk menyusun elemen secara fleksibel baik dalam arah horizontal (baris) atau vertikal (kolom). Flexbox sangat berguna untuk mengatur tata letak yang lebih sederhana, di mana elemen-elemen perlu menyesuaikan ruang yang tersedia pada sumbu utama (main axis).

Kegunaan Flexbox:
Menyusun elemen dalam satu baris atau kolom secara rapi & membuat tata letak elemen secara responsif, di mana elemen bisa tumbuh atau menyusut sesuai dengan ruang yang tersedia.
Contoh penggunaan Flexbox:
css
```css
.container {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}
```

Situasi penggunaan Flexbox:
Menyusun elemen-elemen dalam navbar atau sidebar, menyusun galeri produk dalam satu baris, dan mengatur elemen-elemen dalam satu kolom secara vertikal pada layout mobile.

#### Grid Layout

Grid Layout adalah model layout dua dimensi yang memungkinkan pengaturan elemen secara fleksibel dalam baris dan kolom. Dengan grid, kita bisa mengatur tata letak halaman yang lebih kompleks dan terstruktur.
Kegunaan Grid Layout:
Menyusun elemen pada halaman dalam struktur baris dan kolom  sangat cocok untuk membuat layout yang lebih kompleks seperti dashboard, galeri, atau halaman utama dengan beberapa bagian.
Contoh penggunaan Grid Layout:
Css:
```css
.container {
	display: grid;
	grid-template-columns: 1fr 2fr;
	grid-gap: 30px;
}
```

Situasi penggunaan Grid Layout:
Membuat tata letak halaman web yang kompleks dengan bagian-bagian seperti header, sidebar, konten utama, dan footer, menyusun galeri gambar dalam beberapa baris dan kolom, membuat layout yang responsif dengan struktur grid yang dapat disesuaikan.


### 🟦🟥 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

✅ Implementasikan fungsi untuk menghapus dan mengedit product.

Pertama-tama, saya buat fungsi baru untuk menghapus dan mengedit produk bernama edit_product dan delete_product lalu dimapping di url dengan edit_product/<uuid:id> dan delete_product/<uuid:id>
```python
def edit_product(request, id):
    product = Product.objects.get(pk=id)  

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()  
        return HttpResponseRedirect(reverse('main:ingfo'))  
    
    context = {'form': form}
    return render(request, "edit_product.html", context) 

def delete_product(request, id):
    # Get mood berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:ingfo'))
```

✅ Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
Saya menggunakan Tailwind CSS, maka saya menambahkan tailwind kedalam aplikasi. Kemudian saya membuat tampilan untuk login halaman register, tambah product, dan edit product.
Halaman Login = Form login dengan tampilan responsif dan menggunakan Tailwind untuk styling input field dan tombol submit.
Halaman Register = Form pendaftaran dengan bantuan Tailwind membuat elemen form seperti input dan pesan error memiliki visibility lebih bagus.
Halaman Tambah Produk = Dengan tailwind, penempatan label dan input field lebih konsisten.

✅ Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
saya definisikan komponen HTML baru dalam direktori main/templates/components bernama card_product.html. Kemudian implementasikan kedua button untuk mengedit dan menghapus berupa link yang menuju halaman baru berupa form.
```css
<div class="relative break-inside-avoid">
  <div class="relative top-5 bg-[#7289da] shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-[#5a6bbd] transform rotate-1 hover:rotate-0 transition-transform duration-300">
      <div class="bg-[#7289da] text-white p-4 rounded-t-lg border-b-2 border-[#5a6bbd]">
          <h3 class="font-bold text-xl mb-2">{{ prod_entry.name }}</h3>
      </div>
      <div class="p-4">
          <p class="font-semibold text-lg mb-2 text-white">Product Description</p>
          <p class="text-white mb-2">{{ prod_entry.description }}</p>
          <p class="font-semibold text-lg mb-2 text-white">Price</p>
          <p class="text-white mb-2">${{ prod_entry.price }}</p>

          <div class="flex justify-end space-x-2 mt-4">
              <a href="{% url 'main:edit_product' prod_entry.pk %}" class="bg-[#424549] hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 shadow-md">
                  Edit
              </a>
              <a href="{% url 'main:delete_product' prod_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 shadow-md">
                  Delete
              </a>
          </div>
      </div>
  </div>
</div>
```

✅ Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
saya membuat berkas baru bernama navbar.html dalam direktori templates. Implementasi tampilan responsive
mengimplementasikan dropdown untuk ukuran layar kecil, seperti ukuran layar mobile.

```html
<div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
```
</details>

<details>
  <summary>Tugas 6</summary>

## Tugas 6

### 🟦🟥 Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
  
JavaScript memiliki banyak sekali manfaat. Manfaat utamanya dapat berupa operasi asynchronus, mengubah Document Object Model, membuat web lebih responsif dan dinamis, dll.

Sebagai Contoh:
Kedinamisan dalam kode saya terdapat pada main.html JavaScript digunakan untuk menangani pembukaan dan penutupan modal (showModal() dan hideModal()), serta untuk menangani pengiriman data secara asynchronus (addProductEntry()). Contoh selanjutnya untuk mengubah Document Object Model berupa fungsi refreshProductEntries() menggunakan JavaScript untuk memperbarui konten dalam elemen dengan ID product_entry_cards berdasarkan data dari server.

### 🟦🟥 Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

fetch() adalah metode untuk melakukan permintaan HTTP asynchronus ke server. Seperti fetch, Await digunakan untuk menunggu hasil dari operasi asynchronus. Penggunaan await dan fetch() membuat penulisan kode asynchronus menjadi lebih mudah dibaca dan terstruktur.

tanpa await:
async function getProductEntries() {
  return fetch("{% url 'main:show_json' %}").then((res) => res.json());
}

tanpa await eksekusi kode selanjutnya akan berjalan sebelum data diambil dari server. Akibatnya akan menyebabkan error atau data tidak valid.

Maka dengan await:
async function getProductEntries() {
  const response = await fetch("{% url 'main:show_json' %}");
  return response.json();
}

### 🟦🟥 Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Cross-Site Request Forgery adalah serangan yang memaksa pengguna yang sudah authenticate untuk mengirimkan permintaan yang tidak diinginkan ke aplikasi web. Django tersendiri memiliki pertahanan untuk mencegah hal tersebut. Dengan menggunakan @csrf_exempt digunakan untuk menonaktifkan proteksi CSRF, hal ini berguna saat menggunakan API atau AJAX POST tanpa mengirim token CSRF.

@csrf_exept ditaruh diatas fungsi add_product_entry_ajax:
```python
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
```

### 🟦🟥 Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data input pengguna dilakukan di backend karena keamanan yang lebih kuat sebab data yang dikirim dari frontend dapat lebih mudah dimanipulasi oleh pengguna. Dengan pembersihan di backend, semua data yang diterima telah dibersihkan dari serangan seperti Cross-Site Scripting (XSS), walaupun frontend sudah diubah.
Dengan ini, saya menggunakan  fungsi strip_tags yang diimport dari django.
Sebagai contoh:

```python
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    # ...
```

dan

```python
def clean_product(self):
        product = self.cleaned_data["name"]
        return strip_tags(product)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
```

### 🟦🟥 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

✅Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.

✅ AJAX GET
✅ Ubahlah kode cards data product agar dapat mendukung AJAX GET.

	Untuk mendapatkan objek-objek produk dari endpoint /json, pertama-tama saya menghapus `product_entries = Product.objects.filter(user=request.user)` dan `product_entries': product_entries`, di views.py karena kedua baris tersebut sudah redundant (tidak digunakan lagi). Selanjutnya saya memfilter penampilan pada show_json dan show_xml dengan menambahkan `data = Product.objects.filter(user=request.user)` di baris paling atas fungsi show_json dan show_xml. 
	
	Kemudian, pada main.html, saya menginisialisasi sebuah id baru dengan nama product_entry_cards, membuat fungsi baru didalam block script yang saya namakan `getProductEntries()`, dan menghapus block conditional di product_entries. 

✅ Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data
yang diambil hanyalah data milik pengguna yang logged-in.

Untuk memastikan data hanyalah milik pengguna, pada tugas sebelumnya sudah terdapat  `@login_required(login_url='/login')` yang memastikan kalau dia telah logged-in. Kemudian fungsi show_json yang sudah diubah akan mengembalikan data json milik pengguna yang login. AJAX GET request akan di handle oleh async function getProductEntries() di main.html. `Product.objects.filter(user=request.user)` dalam fungsi show_json memastikan bahwa setiap pengguna hanya dapat mengakses data produk mereka sendiri.

✅ AJAX POST
✅ Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk 
menambahkan product

Di dalam main.html, saya menambahkan sebuah tombol yang akan membuka modal ketika diklik.
Dengan menggunakan `onclick="showModal();"` built in javascript pada tombol akan memanggil showModal() yang dimana modal tersebut berisi form untuk menambahkan produk baru.
Berikut kode implementasinya:
```html
<button
  data-modal-target="crudModal"
  data-modal-toggle="crudModal"
  class="btn bg-[#7289da] hover:bg-[#5a6bbd] text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4"
  onclick="showModal();"
>
  Add New Product Entry by AJAX
</button>
```

✅ Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data.

Saya membuat fungsi view baru di views.py bernama `add_product_entry_ajax`, namun sebelumnya saya mengimpor csrf_exempt dan require_POST karena csrf_exempt karena permintaan dilakukan via AJAX dan view hanya menerima permintaan POST. kedua import tersebut ditaruh diatas fungsi `add_product_entry_ajax` dengan `@csrf_exempt` dan `@require_POST`. Saya juga mengimport dan menngunakan strip_tags di dalam fungsi tersebut guna untuk mencegah serangan XSS.

✅ Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

Saya menambahkan path baru berupa `path('create-ajax/', views.add_product_entry_ajax, name='add_product_entry_ajax'),` di urls.py. Tujuan saya membuat path ini agar request POST ditangani dan fungsi add_product_entry_ajax akan dipanggil.
Berikut snippet implementasinya di kode saya:

```python
urlpatterns = [
	# ... path lainnya
	path('create-ajax/', views.add_product_entry_ajax, name='add_product_entry_ajax'),
]
```

✅ Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.

Di main.html saya membuat function `addProductEntry` yang akan mengirimkan data form ke endpoint /create-ajax/ dengan memanfaatkan fetch dengan POST

Berikut snippet kode yang menangani pengirima form dengan ajax
```html
function addProductEntry() {
    fetch("{% url 'main:add_product_entry_ajax' %}", {
      method: 'POST',
      body: new FormData(document.querySelector('#productEntryForm')),
    }).then((response) => refreshProductEntries());

    document.getElementById('productEntryForm').reset();
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
}
```

Jika proses berhasil, fungsi addProductEtry akan memanggil `refreshProductEntries()` untuk memperbarui daftar produk tanpa harus ngereload halaman

bagian kode yang menangani request POST ke /create-ajax/ dan pemanggilan fungsi add_product_entry_ajax

```html
<form id="productEntryForm">
  <div class="mb-4">
      <label for="name" class="block text-sm font-medium" style="color: #ffffff;">Product Name</label>
      <input type="text" id="nama" name="name" class="mt-1 block w-full rounded-md p-2" style="background-color: #2c2f33; color: #ffffff; border: 1px solid #7289da;" required />
  </div>
  <div class="mb-4">
      <label for="price" class="block text-sm font-medium" style="color: #ffffff;">Price</label>
      <input type="number" id="price" name="price" min="0" class="mt-1 block w-full rounded-md p-2" style="background-color: #2c2f33; color: #ffffff; border: 1px solid #7289da;" required />
  </div>
  <div class="mb-4">
      <label for="description" class="block text-sm font-medium" style="color: #ffffff;">Description</label>
      <textarea id="description" name="description" rows="3" class="mt-1 block w-full rounded-md p-2" style="background-color: #2c2f33; color: #ffffff; border: 1px solid #7289da;" required></textarea>
  </div>
</form>
```

✅ Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan

Tanpa ngereload halaman, halamam utama akan direfresh karena saya mengimplementasikan fungsi  refreshProductEntries di main.html dengan memperbarui daftar produk menggunakan AJAX.
Fungsi refreshProductEntries saya akan mengambil data produk terbaru menggunakawn getProductEtries() yg mengirimkan request ke AJAX GET di /json. refreshProdukEntries kemudian akan mengupdate elemen menjadi baru dengan ID product_entry_cards utk menampilkan daftar produk terbaru tanpa ngereload seluruh halaman.

Berikut snippet kode saya:

```html
async function refreshProductEntries() {
    document.getElementById("product_entry_cards").innerHTML = "";
    document.getElementById("product_entry_cards").className = "";
    const productEntries = await getProductEntries();
    let htmlString = "";
    let classNameString = "";

    if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data product pada Etrean Luminant Store.</p>
            </div>
        `;
    } else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        productEntries.forEach((item) => {
          const name = DOMPurify.sanitize(item.fields.name);
          const price = DOMPurify.sanitize(item.fields.price);
          const description = DOMPurify.sanitize(item.fields.description);

          htmlString += `
          <div class="relative break-inside-avoid">
              <div class="relative top-5 bg-[#7289da] shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-[#5a6bbd] transform rotate-1 hover:rotate-0 transition-transform duration-300">
                  <div class="bg-[#7289da] text-white p-4 rounded-t-lg border-b-2 border-[#5a6bbd]">
                      <h3 class="font-bold text-xl mb-2">${name}</h3>
                  </div>
                  <div class="p-4">
                      <p class="font-semibold text-lg mb-2 text-white">Product Description</p>
                      <p class="text-white mb-2">${description}</p>
                      <p class="font-semibold text-lg mb-2 text-white">Price</p>
                      <p class="text-white mb-2">$${price}</p>
                  </div>
                  <div class="flex justify-end space-x-2 mt-4 p-4">
                      <a href="/edit_product/${item.pk}" class="bg-[#424549] hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 shadow-md">
                          Edit
                      </a>
                      <a href="/delete_product/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 shadow-md">
                          Delete
                      </a>
                  </div>
              </div>
          </div>`;
      });
    }
    document.getElementById("product_entry_cards").className = classNameString;
    document.getElementById("product_entry_cards").innerHTML = htmlString;
}
```
  </details>