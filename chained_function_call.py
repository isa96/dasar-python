def tambah(a,b):
    return a+b
def kali(a,b):
    return (a*b)

x, y = 1, 2
kondisi = True
hasil = (tambah if kondisi else kali)(x,y)
print(f'hasil:{hasil}')