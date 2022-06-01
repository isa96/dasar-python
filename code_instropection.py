'''
Introspeksi kode adalah kemampuan untuk memeriksa kelas, fungsi, dan kata kunci 
untuk mengetahui apa itu, apa yang mereka lakukan, dan apa yang mereka ketahui.
'''

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))
print(help(Vehicle))
#print(hasattr(Vehicle))
print(id(Vehicle))
print(type(Vehicle))
print(repr(Vehicle))
print(callable(Vehicle))
#print(issubclass(Vehicle))
#print(isinstance(Vehicle))
print(__name__)
print(__doc__ )


 

 

