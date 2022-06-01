mylist = [i for i in range(1, 21)]
print(f'mylist = {mylist}')

# With IF
list1 = [3, 4, 5]
list2 = [item for item in list1 if item > 3]
print(f'list1:{list1}')
print(f'list2:{list2}')

# With Zip
aaa = ['aaa', 'ccc', 'xxx']
bbb = ['12', '34', '43']
ddd = [[data_aaa, data_bbb] for data_aaa, data_bbb in zip(aaa, bbb)]
print(f'ddd:{ddd}')