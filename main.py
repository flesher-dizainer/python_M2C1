# Задание 1
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.
def task_1():
    try:
        a = int(input('Enter the first number of the number range: '))
        b = int(input('Enter the end number of the number range: '))
        for i in range(a,b+1):
            if i % 7 == 0:
                print(i)
    except ValueError:
        print("Input value error")

# Задание 2
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

def task_2():
    try:
        a = int(input('Enter the first number of the number range: '))
        b = int(input('Enter the end number of the number range: '))
        count_div_5 = 0
        number_div_7 = ''
        all_value = ''
        value_end_to_first = ''
        for i in range(a,b+1):
            all_value +=str(i)+' '
            value_end_to_first += str(b - i) + ' '
            if i % 7 == 0:
                number_div_7 += str(i) + ' '
            if i % 5 == 0:
                count_div_5 += 1
        print('All number value =',all_value)
        print('Numbers in descending order =', value_end_to_first)
        print('All number multiples of 7 =',number_div_7)
        print('Count number multiples of 5 =',count_div_5)
    except ValueError:
        print("Input value error")

# Задание 3
# Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# Требуется проанализировать все числа в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# Если число кратно 5 нужно вывести слово Buzz.
# Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.
def task_3():
    try:
        a = int(input('Enter the first number of the number range: '))
        b = int(input('Enter the end number of the number range: '))
        for i in range(a,b+1):
            if ( i % 3 == 0 ) and ( i % 5 == 0 ):
                print('Fizz','Buzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
    except ValueError:
        print("Input value error")


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()