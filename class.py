'''
Objek adalah enkapsulasi(mengisolasi) variabel dan fungsi menjadi satu kesatuan. 
Objek mendapatkan variabel dan fungsinya dari kelas. 
Kelas pada dasarnya adalah contoh untuk membuat objek.
'''

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

# Cara akses objek variabel
print(myobjectx.variable)

myobjecty = MyClass()
myobjecty.variable = "yackity"
print(myobjecty.variable)