def say_hai(nama):
    return f"hai {nama}"
def total (*list_angka):
    hasil=0
    for data in list_angka:
        hasil = hasil + data
    return hasil