#Menampilkan hasil return dengan data lebih dari 1 
# maka gunakan tipe data tuple

def aaa(*bbb):
    t = 0
    for cc in bbb:
        t = t + cc
    return (bbb, t)
bbb, t = aaa(12, 10, 1, 1, 3)
print(f"t {bbb} = {t}")