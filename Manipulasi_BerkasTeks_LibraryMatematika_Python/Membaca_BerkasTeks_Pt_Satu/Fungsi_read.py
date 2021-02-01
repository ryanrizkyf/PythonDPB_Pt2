# file hello.txt
# Kita sedang belajar Python
# Tepatnya belajar memanipulasi berkas teks
# Memanipulasi berkas dengan Python sangatlah mudah!


# Membaca file hello.txt dengan fungsi read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open("hello.txt", "r")
content = file.read()
file.close()
print(content)


# hasil
# Kita sedang belajar Python
# Tepatnya belajar memanipulasi berkas teks
# Memanipulasi berkas dengan Python sangatlah mudah!
