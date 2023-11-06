N_LIMIT = 100000
NUMBER_LIMIT = 1000000000

print('Введите число N от 1 до 100 000')
n = int(input('N = '))
if n < 0 or n > N_LIMIT:
    print('Значение N введено не верно')
else:
    print(f'Введите чисел = {n} от 1 до 1е9 через пробел')
    number = list(map(int, input().split()))
    numberLength = len(number)
    if numberLength != n: 
        print(f'Количество введенных значении не совпадает с N ({n} не равно {numberLength})')
    else:
        for i in range(numberLength):
            if number[i] < 1 or number[i] > NUMBER_LIMIT:
                print(f'Число {number[i]} выходит за допустимы диапазаон')
                break
        rezultArray = []

        rezultArray.append(number[numberLength - 1])
        for i in range(numberLength - 1):
            rezultArray.append(number[i])

        print(rezultArray)