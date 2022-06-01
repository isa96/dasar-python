from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

# Note: nilai default akan mulai mengganti variabel dari kiri. 
#       2 akan menggantikan x. y akan sama dengan 4 ketika dbl(4) dipanggil.