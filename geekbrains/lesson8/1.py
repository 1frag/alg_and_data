str_ = input('Введите строку:\n')
set_ = set()
size_ = len(str_)
for i in range(size_):
    for j in range(i, size_):
        set_.add(hash(str_[i:j+1]))
print(f'{len(set_)} - именно столько различных подстрок в строке')

print('Не обманул ли?')
set_ = set()
for i in range(size_):
    for j in range(i, size_):
        set_.add(str_[i:j+1])
numb = 1
for q in set_:
    print(f'{numb}) {q}')
    numb += 1
