# file hello.txt
# Kita sedang belajar Python
# Tepatnya belajar memanipulasi berkas teks
# Memanipulasi berkas dengan Python sangatlah mudah!


# Menulis ke file hello_write.txt
file = open("hello.txt", "w")
file.write("Sekarang kita belajar menulis dengan menggunakan Python")
file.write("Menulis konten file dengan mode w (write).")
file.close()
