# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X

N = abs(int(input('Введите количество элементов массива : ')))
element = input("Введите через пробел элементы массива: ").split()
num = list(map(int, element))
if len(num) != N:
    print('Введенные элементы не соответствуют необходимому количеству.')
else:
    X = int(input('Введите число X, которое необходимо найти в массиве: '))
    count = 0
    for i in range(N):
        if num[i] == X:
            count += 1
    print(f'Число {X} встречается в массиве {count} раз') 
    