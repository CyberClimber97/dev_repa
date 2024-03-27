import json
from pprint import pprint
# PART 1

#1
x = float(input('Вклад: '))
p = float(input('Процент: '))
y = float(input('Итоговая сумма: '))
years = 0

while x < y:
    x = x*(p*0.01) + x
    years += 1
    print(years)


#2
n = int(input('Число повторений: '))
count = 1

while count <= n:
    count += 1
    print('for - частный случай while')

#____________________________________________________________

# PART 2

#1
l = [1, 2, 2, 'hello', 'hello']
l2 = []
for i in l:
    if i in l2:
        continue
    else:
        l2.append(i)
print(l2)

#2
from random import randint
n = int(input('Enter a number: '))
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
pprint (m)
max = -2147483648

for i in m:
    for j in i:
        if j > max:
            max = j

print(max)

#3
d = {'key1': 'value1', 'key2': 'value2'}
a: dict = {}

for k, v in d.items():
    a[v] = k
print(a)

#____________________________________________________________

# PART 3

#1
def area(a, b, c):
    s =(a + b + c) / 2
    area =(s*(s-a)*(s-b)*(s-c)) ** 0.5

    print(area)

#2

rand_string = 'Я памятник себе воздвиг нерукотворный'

def five_and_more_word_strig(rand_string):
    new_string = ''
    list_of_words = rand_string.split()
    for i in list_of_words:
        if len(i) <= 5:
            new_string = (f'{new_string} {i}')

    print(new_string)

five_and_more_word_strig('Я памятник себе воздвиг нерукотворный')

#____________________________________________________________

# PART 4

#1

def register(login, password):
    a = {login:password}
    with open ('users.txt', 'w') as f:
        json.dump(a, f)

register('a', 'asd')

#2


def register2(login, password):
    with open('users.txt', 'r') as f:
        data = json.load(f)
        if login not in data.keys():
            data[login] = password
            with open('users.txt', 'w') as f:
                json.dump(data, f)
        else:
            print('login already registered')


register2('aa', 'qwer')

