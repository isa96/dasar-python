import function
#cara lain panggil fungsi di sebuah module 
# from function import say_hai 
# from function import total
# kalo pakai cara di atas maka tidak perlu menyebutkan prefixnya
# Jadi: hai =  say_hai("aaa")
# Jadi: hasil = total(9,9,9)
hai =  function.say_hai("aaa")
print(hai)
hasil = function.total(9,9,9)
print(hasil)