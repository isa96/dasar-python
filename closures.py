'''
Closure ialah fungsi objek yang bisa mengingat suatu nilai di dalam scope 
meskipun tidak ada dalam memori nilai tersebut.
Contoh sederhana closure adalah Nested Function yang mana adalah
fungsi yang didefinisikan di dalam fungsi lain.
Nested Function dapat mengakses variabel dari lingkup scopenya
menggunakan kata kunci "nonlokal" secara eksplisit dapat memodifikasi perubahan sebuah variable
yang ada dalam scope.
'''

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))

# Nonlocal
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

# Tanpa nonlokal hasilnya seharusnya 3 dan 9. Karena di setting nonlocal setiap ada perubahan dari luar scope 
# maka dia akan merubahnya ke nilai variabel di local nya