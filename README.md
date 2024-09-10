## Nama : Argya Farel Kasyara
## NPM : 2306152424
## Kelas : PBP C

## Tautan PWS :

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#### a. Untuk membuat proyek Django baru, hal yang pertama yang dilakukan adalah membuat direktori baru dengan nama "warung-imut" sebagai folder proyek. Setelah itu, saya buat repositori git baru dengan command "git init". Saya buat virtual environment python lalu saya install library-library yang akan dibutuhkan dan akhirnya saya jalankan command "django-admin startproject warung_imut". Hal ini akan membuat proyek Django. Saya juga tambahkan dua string ("localhost", "127.0.0.1") pada ALLOWED_HOSTS di settings.py.
#### b. Untuk membuat aplikasi dengan nama main dalam proyek, saya lakukan command "python manage.py startapp main" pada direktori warung-imut utama. 
#### c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main dapat diimplementasikan  dengan menambahkan 'main' pada variabel INSTALLED_APPS di settings.py. 
#### d. Membuat model pada aplikasi main dengan ketentuan tugas dapat diimplementasikan dengan mendefinisikan sebuah class Item yang inherit dari Django model lalu memberikan attribute yang sesuai di file models.py pada direktori main.
#### e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML dapat diimplementasikan dengan mendefinisikan fungsi yang mengembalikan render template HTML sesuai dengan konteks yang diberikan. Konteks disini adalah nama, kelas, dan npm.
#### f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py dapat diimplementasikan dengan membuat list yang berisikan path ke fungsi yang ada di views.py urls = [path('', show_main, name='show_main')]
#### g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet dapat dilakukan dengan

#### h. Membuat README.md sesuai dengan perintah soal dengan mempelajari materi yang terkait dengan pertanyaan dan menjawabnya dengan baik

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
####

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
#### a. Git berperan sebagai version control system yang membantu developer dalam mengatur dan melacak perubahan dalam kode. Hal ini membuatnya penting dalam kolaborasi antara banyak developer, sehingga masing-masing developer dapat berkontribusi dengan baik. 
#### b. Pemberian arsitektur tersebar sehingga setiap developer memiliki salinan sejarah dari proyek yang sedang dibuatnya. Jika salah satu developer kehilangan proyek, salinannya masih ada di orang lain.
#### c. Memudahkan perbaikan kesalahan. Git memungkinkan developer untuk membatalkan perubahan atau kembali ke versi sebelumnya jika terjadi bug atau kesalahan yang tidak diingkan.
#### d. Memfasilitasi review kode. Git memfasilitasi peer review dengan memungkinkan developer untuk memerika atau mengomentari kode orang lain melalu pull request.
#### e. Git memungkinkan developer untuk membuat branches dengan fitur baru atau memperbaiki bug tanpa memperangurhi tempat kode utama. Setelah branches ini sudah selesai dan dites maka branches tersebut dapat dikembalikan kembali ke kode utama.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
#### a. Dikarenakan Django sangat-sangat populer dan banyak sekali tutorial-tutorial untuk mempelajarinya. Hal ini membuat  kita sebagai pelajar mudah dan cepat untuk memahaminya
#### b. Memiliki struktur yang jelas dan konsisten. Django mengikuti arsitektur Model-View-Template (MVT) yang memisahkan bagian-bagian web dengan jelas sehingga kita dapat dengan mudah memahaminya.
#### c. Django menggunakan bahasa pemrograman yang sangat popular dan memiliki sintaks yang cukup mudah yaitu Python. Hal ini membuat kita lebih fokus terhadap konsep-konsep yang dipelajari dibandingkan mempelajari sintaks.
#### d. Django sudah menyertakan perlindungan bawaan terhadap kerentanan umum seperti injeksi SQL dan lain-lain. Hal ini membantu pemula menulis kode aman dan membuat pemula tidak perlu terlalu fokus terhadap aspek ini melainkan terhadap aspek-aspek web.
#### e. Django sangat lengkap dan comprehensive untuk membuat web dan bisa digunakan oleh aplikasi skala besar. Django juga mendorong penulisan kode yang efisien dan bersih dengan menghindari duplikasi. Hal ini akan menanam kebiasaan yang baik dalam menulis kode.

### 5. Mengapa model pada Django disebut sebagai ORM?
#### Karena Django menyediakan abstraksi yang memungkinkan developer untuk berinteraksi dengan basis data relasional menggunakan objek Python, daripada menulis kueri SQL mentah saja. Django ORM mengabstraksikan kueri SQL dan menyedikan cara yang lebih "Python" untuk bekerja dengan basis data.