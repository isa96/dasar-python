''' Ketika kondisi loop dari pernyataan "for" atau "while" gagal maka bagian kode di "else" dijalankan. 
    Jika pernyataan "break" dieksekusi di dalam for loop maka bagian "else" akan dilewati. 
    Perhatikan bahwa bagian "else" dijalankan bahkan jika ada pernyataan lanjutan (continue). '''
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")