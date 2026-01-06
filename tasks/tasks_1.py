# 1) Определить,является ли введенное пользователем число - простым

a = int(input("Введи число: "))
k = 0
delit = []
for i in range(1, a + 1):
    if a % i == 0:
        k += 1
        delit.append(i)
if k == 2:
    print("Число простое")
else:
    print("Число непростое")
print(delit)

# 2) Найти сумму цифр введенного числа

a = int(input("Введи число: "))
s = 0
while a > 0:
    s += a % 10
    a = a // 10
print(s)

# 3) Дан список чисел. Превратите его в список квадратов этих чисел

sp = [7, 8, 9, 4, 8]

s1 = []
for x in sp:
    s1.append(x**2)

s1 = [x**2 for x in sp] # генератор списоков
print(s1)

# 4) Вводится строка.Требутся удалить из нее повторяющиееся символы и все пробелы

s = input("Введите строку: ")
s_new = ''

for x in s:
    if x not in s_new and x != ' ':
        s_new += x
print(s_new)

# 5) Вводится строка состоящая из слов,разделенных пробелами.Требутся посчитать кол-во слов в ней

s = input("Введите строку: ")
k = 0
for x in s:
    if x == ' ':
        k += 1

print(len(s.split()))

# 6) найти уравнение прямой (y=kx+b) проходящей через две известные точки
print('A(x1; y1)')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('B(x2; y2)')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Уравнение: ')

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x1
print('\ty = %.2f*x + %.2f' % (k, b))


# 7) Поменять пордяок цифр числа на обратный

n1 = int(input('Введите число: '))
n2 = 0

while n1 > 0:
    digital = n1 % 10
    print(digital)
    n1 //= 10
    print(n1)
    n2 *= 10
    n2 += digital
print(n2)
