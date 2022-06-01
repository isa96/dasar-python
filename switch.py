def one():
    print('aaa')
def two():
    print('bbb')

case = 'dua'
switch = {
    'satu':one,
    'dua':two
}
switch[case]()
