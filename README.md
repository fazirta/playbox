# PlayBox

PlayBox is a Django e-commerce site for gaming gear and accessories. It offers a user-friendly interface for browsing and purchasing gaming products, with a focus on delivering an engaging shopping experience.

### Tech Stack

- **Backend**: Django
- **Styling**: TailwindCSS
- **Hosting**: Pacil Web Service (PWS)

### Deployment

Explore the live version here: [PlayBox](http://muhammad-fazil31-playbox.pbp.cs.ui.ac.id/)

---

## Tugas 2 PBP Gasal 2024/2025

### Implementasi Checklist Tugas Secara Step-by-Step

#### 1. Membuat Proyek Django Baru

Langkah pertama yang saya lakukan adalah membuat proyek Django baru. Saya menggunakan perintah `django-admin startproject` untuk menginisialisasi proyek dengan nama `playbox`. Perintah ini menciptakan struktur dasar proyek Django yang meliputi beberapa file konfigurasi dan folder.

```bash
django-admin startproject playbox .
```

#### 2. Membuat Aplikasi `main`

Setelah proyek berhasil dibuat, langkah berikutnya adalah menambahkan aplikasi baru dengan nama `main`. Dalam Django, aplikasi adalah bagian modular dari proyek yang memungkinkan pengembangan fitur secara terpisah. Saya menjalankan perintah `python manage.py startapp main` untuk membuat aplikasi `main`.

```bash
python manage.py startapp main
```

#### 3. Mengonfigurasi Routing untuk Aplikasi `main`

Selanjutnya, saya harus mengonfigurasi routing proyek untuk menyertakan aplikasi `main`. Dalam file `urls.py` proyek, saya menambahkan routing untuk aplikasi `main` dengan menggunakan fungsi `include` agar aplikasi dapat mengelola URL-nya sendiri. Kode yang saya tambahkan adalah sebagai berikut:

```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

#### 4. Membuat Model `Product` pada Aplikasi `main`

Untuk menyimpan data produk, saya mendefinisikan sebuah model `Product` dalam file `models.py` aplikasi `main`. Model ini mencakup atribut-atribut seperti `name`, `price`, `description`, dan `stock`. Saya juga menambahkan `created_at` dan `updated_at` untuk melacak waktu pembuatan dan pembaruan. Berikut adalah kode model yang saya buat:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.PositiveIntegerField()
    image = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

#### 5. Membuat Fungsi View di `views.py`

Saya kemudian membuat sebuah view dalam file `views.py` yang bertugas untuk merender template HTML. Fungsi `landing` ini akan menampilkan template yang menunjukkan nama aplikasi serta nama dan kelas. Berikut adalah kode untuk fungsi view tersebut:

```python
from django.shortcuts import render

def landing(request):
    return render(request, "landing/index.html")
```

#### 6. Menambahkan Routing di `urls.py` Aplikasi `main`

Untuk memastikan bahwa view `landing` dapat diakses melalui URL tertentu, saya menambahkan routing di `urls.py` aplikasi `main`. Routing ini mengarahkan URL root ('') ke fungsi `landing`. Kode yang saya tambahkan adalah sebagai berikut:

```python
from django.urls import path
from main.views import landing

urlpatterns = [
    path('', landing, name='landing'),
]
```

#### 7. Deployment melalui Platform Web Services (PWS)

Terakhir, saya melakukan deployment aplikasi ke Platform Web Services (PWS). Prosesnya meliputi beberapa langkah:

##### 7.1. Membuat Proyek Baru di PWS

Saya memulai dengan mengklik "Create New Project" pada dashboard PWS dan mengisi kolom `Project Name` dengan nama `playbox`. Saya kemudian mengklik "Create New Project" untuk menyelesaikan proses pembuatan proyek.

##### 7.2. Menambahkan URL pada `settings.py`

Dalam file `settings.py`, saya menambahkan URL deployment PWS ke dalam daftar `ALLOWED_HOSTS` untuk mengizinkan akses dari domain tersebut:

```python
...
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "muhammad-fazil31-playbox.pbp.cs.ui.ac.id"]
...
```

##### 7.3. Menjalankan Perintah Deployment

Saya menjalankan perintah yang tercantum pada bagian "Project Command" di halaman PWS. Saat melakukan push ke PWS, saya memasukkan username dan password yang diberikan oleh PWS.

##### 7.4. Memantau Status Proyek dan Akses URL Deployment

Di dashboard PWS, saya memantau status proyek yang saya buat. Jika statusnya "Building", berarti proyek masih dalam proses deployment. Jika statusnya "Running", berarti proyek telah berhasil dideploy dan dapat diakses melalui URL yang diberikan. Untuk melihat hasilnya, saya menekan tombol "View Project".

---

### Bagan Request dan Respon Web Aplikasi Django

Berikut adalah bagan sederhana yang menggambarkan alur request client ke web aplikasi berbasis Django beserta responnya serta hubungan antara `urls.py`, `views.py`, `models.py`, dan berkas HTML:

```
Client Request (e.g., GET /) 
        |
        v
      urls.py
        |
        v
      views.py
        |
        v
      models.py (jika diperlukan untuk data)
        |
        v
     HTML Template
        |
        v
    Client Response (HTML)
```

#### Penjelasan Bagan:

1. **Client Request**: Client (misalnya, browser) mengirimkan request ke server, seperti permintaan untuk halaman utama ('/').

2. **urls.py**: Django menerima request dan mencocokkan URL dengan routing yang didefinisikan di `urls.py`. Jika URL cocok, Django akan meneruskan request ke view yang sesuai.

3. **views.py**: View yang sesuai (misalnya, `landing`) akan dipanggil untuk menangani request. View ini bisa melakukan logika tambahan atau berinteraksi dengan model.

4. **models.py**: Jika view memerlukan data dari database, view akan menggunakan model yang didefinisikan di `models.py` untuk berinteraksi dengan database.

5. **HTML Template**: View merender template HTML dengan data yang diambil. Template ini adalah file HTML yang berisi struktur halaman web.

6. **Client Response**: Hasil render dari template HTML dikirim kembali sebagai respons ke client.

---

### Fungsi Git dalam Pengembangan Perangkat Lunak

Git adalah sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak. Git memungkinkan pengembang untuk melacak perubahan pada kode sumber seiring berjalannya waktu. Beberapa fungsi utama Git dalam pengembangan perangkat lunak adalah:

- **Version Control**: Git memungkinkan pengembang untuk melacak versi berbeda dari kode sumber, memudahkan untuk kembali ke versi sebelumnya jika diperlukan.
- **Branching and Merging**: Pengembang dapat membuat cabang (branch) untuk fitur baru atau perbaikan tanpa mempengaruhi kode utama. Setelah selesai, cabang dapat digabungkan (merge) kembali ke branch utama.
- **Collaboration**: Git mendukung kolaborasi antara beberapa pengembang dengan memungkinkan mereka untuk bekerja pada repositori yang sama secara bersamaan tanpa konflik.
- **History Tracking**: Git menyimpan riwayat perubahan, termasuk siapa yang membuat perubahan dan kapan perubahan tersebut dibuat, membantu dalam audit dan debugging.

---

### Mengapa Framework Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Django sering dipilih sebagai framework pemula dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan:

- **Struktur dan Konvensi**: Django menyediakan struktur yang jelas dan mengikuti prinsip "konvensi di atas konfigurasi", yang membantu pemula memahami arsitektur aplikasi web.
- **Dokumentasi dan Komunitas**: Django memiliki dokumentasi yang sangat baik dan komunitas yang besar, sehingga memudahkan pemula untuk menemukan bantuan dan solusi.
- **Fitur Bawaan**: Django dilengkapi dengan banyak fitur bawaan seperti autentikasi pengguna, panel admin, dan ORM, yang mempercepat pengembangan aplikasi tanpa harus membangun fitur-fitur dasar dari nol.
- **Keamanan**: Django secara default mengikuti praktik keamanan yang baik, mengurangi risiko kerentanan yang umum dalam pengembangan aplikasi web.

---

### Mengapa Model pada Django Disebut sebagai ORM?

Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ORM untuk memetakan objek Python ke tabel-tabel dalam database relasional. Dengan ORM, saya dapat menggunakan kode Python untuk berinteraksi dengan database tanpa menulis SQL secara langsung. ORM memudahkan operasi database seperti penyimpanan, pengambilan, pembaruan, dan penghapusan data melalui objek Python, sehingga meningkatkan produktivitas dan meminimalkan kemungkinan kesalahan.

---

## Tugas 3 PBP Gasal 2024/2025

### Pentingnya Data Delivery dalam Platform

**Data delivery** adalah proses menyampaikan data dari server ke client. Ini penting karena:

- **Interaksi Dinamis**: Aplikasi sering membutuhkan data terbaru yang dapat dikirim secara real-time atau sesuai permintaan dari client.
- **Efisiensi dan Responsivitas**: Data delivery memastikan bahwa client mendapatkan data yang relevan dan terkini dengan cara yang efisien.
- **Pengalaman Pengguna**: Pengalaman pengguna menjadi lebih baik ketika data dapat disampaikan dengan cepat dan akurat.

### XML vs JSON

**XML** dan **JSON** adalah format untuk pertukaran data. JSON lebih populer dibandingkan XML karena:

- **Sintaks yang lebih sederhana**: JSON lebih ringkas dan mudah dibaca daripada XML.
- **Ukuran yang lebih kecil**: JSON biasanya menghasilkan file yang lebih kecil karena tidak memerlukan tag penutup seperti XML.
- **Penggunaan yang luas dalam web dan API**: JSON lebih mudah diintegrasikan dengan JavaScript dan banyak API modern menggunakan JSON karena kemudahan penggunaannya.

### Fungsi `is_valid()` pada Form Django

**`is_valid()`** adalah metode pada form Django yang digunakan untuk memeriksa apakah data yang dikirimkan memenuhi semua validasi yang ditentukan dalam form. 

- **Fungsi**: Mengembalikan `True` jika data form valid dan `False` jika tidak. Ini memeriksa validitas data berdasarkan aturan yang didefinisikan dalam form.
- **Kebutuhan**: Memastikan bahwa data yang diproses aman dan sesuai dengan harapan sebelum disimpan atau diproses lebih lanjut.

### CSRF Token di Django

**CSRF Token** adalah mekanisme untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF). 

- **Kebutuhan**: Token CSRF diperlukan untuk memastikan bahwa permintaan yang dikirimkan ke server berasal dari pengguna yang sah.
- **Tanpa Token**: Jika tidak ada token CSRF, penyerang dapat membuat permintaan berbahaya menggunakan kredensial pengguna yang sah.
- **Potensi Risiko**: Penyerang dapat memanfaatkan kurangnya perlindungan CSRF untuk melakukan tindakan tidak sah seperti mengubah data pengguna atau mengirimkan permintaan yang merugikan.

### Implementasi Checklist Secara Step-by-Step

#### 1. Membuat input form untuk menambahkan objek model pada app sebelumnya

Pertama, saya membuat berkas `forms.py` dengan kode yang mendefinisikan struktur form untuk Product, lalu menambahkan kode pada `views.py` untuk menangani form tersebut, serta memperbarui fungsi `show_main` untuk menampilkan seluruh Product. Saya juga mengupdate `urls.py` untuk menambahkan path ke fungsi `create`, membuat berkas HTML `create/index.html` untuk form input, dan menyesuaikan `main.html` agar menampilkan data product dalam tabel serta menambahkan tombol untuk mengakses form input.

#### 2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID

Saya mengembalikan data dalam bentuk XML dan JSON dengan beberapa langkah. Pertama, saya membuka `views.py` dan menambahkan import `HttpResponse` dan `serializers`. Saya membuat fungsi `show_xml` untuk mengembalikan seluruh data MoodEntry dalam format XML dan fungsi `show_json` untuk mengembalikan data yang sama dalam format JSON. Setelah itu, saya memperbarui `urls.py` untuk menambahkan path URL yang sesuai. Selanjutnya, saya membuat fungsi `show_xml_by_id` dan `show_json_by_id` untuk mengembalikan data MoodEntry berdasarkan ID dalam format XML dan JSON, kemudian menambahkan path URL untuk kedua fungsi ini di `urls.py`.

#### 3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2

Saya menambahkan path URL ke dalam urlpatterns di berkas urls.py untuk menghubungkan URL yang sesuai dengan fungsi view yang telah dibuat. Saya menambahkan path `"xml/"` untuk format XML dan `"json/"` untuk format JSON. Untuk data berdasarkan ID, saya menambahkan path `"xml/<str:id>/"` dan `"json/<str:id>/"`.

Berikut adalah pengaturan urlpatterns yang saya buat:

```python
urlpatterns = [
    ...
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>/", show_json_by_id, name="show_json_by_id"),
    ...
]
```

### Mengakses URL dengan Postman
**XML**
![image](https://github.com/user-attachments/assets/c09ca1e5-db92-46b6-ae97-1d584f807860)

**JSON**
![image](https://github.com/user-attachments/assets/4eac9827-7ab0-4e6f-82e9-4ce82cb3c3a9)

**XML by ID**
![Screenshot (13)](https://github.com/user-attachments/assets/5304e958-ea84-4a4b-a5c4-a642f332ae28)

**JSON by ID**
![Screenshot (14)](https://github.com/user-attachments/assets/3a3ea9c4-e303-4d48-aead-3a32d27a689f)

---

## Tugas 4 PBP Gasal 2024/2025

### Apa perbedaan antara HttpResponseRedirect() dan redirect()?

`HttpResponseRedirect()` adalah kelas untuk membuat respon HTTP yang mengarahkan ke URL lain, sedangkan `redirect()` adalah shortcut yang menyederhanakan penggunaan `HttpResponseRedirect()` dan dapat menerima URL atau model instance.

### Jelaskan cara kerja penghubungan model Product dengan User!

Model Product memiliki field ForeignKey yang menunjuk ke model User, sehingga setiap produk terkait dengan pengguna tertentu. Ini memungkinkan kita untuk mengaitkan setiap produk dengan pemiliknya.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login?

Authentication adalah proses verifikasi identitas pengguna (login), sedangkan authorization menentukan hak akses pengguna tersebut. Saat pengguna login, sistem melakukan authentication dengan memeriksa kredensialnya. Django mengimplementasikan ini melalui sistem autentikasi built-in.

### Bagaimana Django mengingat pengguna yang telah login?

Django menggunakan session untuk menyimpan informasi tentang pengguna yang login, dan secara otomatis mengatur cookie untuk menjaga session tersebut. Kegunaan lain dari cookies termasuk menyimpan preferensi pengguna dan informasi terakhir login. Tidak semua cookies aman; cookie harus disimpan dengan aman dan tidak boleh mengandung informasi sensitif.

### Implementasi Checklist Secara Step-by-Step

#### 1. Mengimplementasikan registrasi, login, dan logout agar pengguna dapat mengakses aplikasi

Saya mulai dengan mengaktifkan virtual environment, kemudian menambahkan import di `views.py` untuk `UserCreationForm`, `AuthenticationForm`, dan fungsi login/logout. Selanjutnya, saya membuat fungsi `register` untuk menangani pendaftaran pengguna, membuat berkas `register.html`, dan memperbarui `urls.py`. Setelah itu, saya menambahkan fungsi `login_user` dan membuat **`login.html`** serta memperbarui `urls.py` untuk login. Terakhir, saya menambahkan fungsi `logout_user`, membuat tombol logout di **`main.html`**, dan memperbarui `urls.py` untuk logout.

#### 2. Membuat dua akun pengguna dengan tiga data dummy per akun

Untuk membuat akun, saya hanya perlu melakukan registrasi dua kali dengan informasi pengguna yang berbeda. Setelah itu, untuk membuat dummy data, saya login dengan akun yang diinginkan. Setelah berhasil masuk, saya dapat menambahkan dummy data baru melalui form yang sudah dibuat pada Tugas 3 sebelumnya.

**Pengguna 1 (peokra)**
![peokra](https://github.com/user-attachments/assets/ff68b75d-1a8e-4e66-b098-3d63f3e6d1f8)

**Pengguna 2 (pakbepe)**
![pakbepe](https://github.com/user-attachments/assets/20ef2db9-52bb-4754-ae41-1f9e2e1f23c7)

#### 3. Menghubungkan model `Product` dengan `User`

Saya menambahkan atribut user pada model Product, yang merupakan *ForeignKey* yang merujuk pada model User. Dengan cara ini, setiap produk akan terkait langsung dengan pengguna tertentu. Saya menggunakan parameter on_delete=models.CASCADE untuk memastikan bahwa jika seorang pengguna dihapus, semua produk yang mereka buat juga akan dihapus secara otomatis. Ini menjaga database saya tetap bersih dan teratur.

Berikut adalah implementasi lengkap dari model `Product`:

```python
class Product(models.Model):
    ...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

#### 4. Menampilkan username pengguna yang logged in dan cookies last login
Pertama, saya mengedit `views.py` dengan menambahkan import yang diperlukan. Dalam fungsi `signin`, saya mengubah kode agar menambahkan cookie "last_login" dengan waktu saat pengguna login. Di fungsi `landing`, saya menambahkan informasi cookie ke dalam konteks. Kode `request.user.username` saya gunakan untuk menampilkan username pengguna di halaman utama. Saya juga menambahkan informasi cookie ke dalam *context*. Selain itu, saya mengubah fungsi `logout` untuk menghapus cookie saat logout. Terakhir, saya memperbarui `profile/index.html` untuk menampilkan sesi terakhir login.