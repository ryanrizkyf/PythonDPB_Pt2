# file hello.txt
# Kita sedang belajar Python
# Tepatnya belajar memanipulasi berkas teks
# Memanipulasi berkas dengan Python sangatlah mudah!


# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)


# hasil
# [“Kita sedang belajar Python”, “Tepatnya belajar memanipulasi berkas teks”, “Memanipulasi berkas dengan Python sangatlah mudah!”]
