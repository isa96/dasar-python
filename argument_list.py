# * Menandakan Argument List
# Argument list hanya bisa digunakan 1 kali
# Jika ingin menambahkan default paramater 
# maka harus di taruh di depan 
# contoh def aaa(x, *bbb):
def aaa(*bbb):
    t = 0
    for cc in bbb:
        t = t + cc
    print(f"t {bbb} = {t}")
aaa(12, 10, 1, 1, 3)