#Menggunakan Dictionary untuk mengambil data 
#bukan dengan index melainkan dari key nya
#pada Dictionary terdapat method/fuction items()
#items() memliki output tipe data tuple
aaa = {"nama": "bbb", "age":10, "alamat": "solo"}

#cara nambah data Dictionary
aaa["company"] = "y"

#cara ganti data Dictionary
aaa["nama"] = "ccc"

#cara hapus data Dictionary
del aaa["alamat"]
#cara hapus yang ke 2
aaa.pop["alamat"]

for key,value in aaa.items():
    print(f"{key}:{value}")