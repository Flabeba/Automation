my_age = input("Какаой у вас возвраст?: ")          #Задаю переменную и присваиваю input(Ввод чего либо в терминале)          
my_age = int(my_age)            # Присваиваю переменной формат int(формат числа) Это нужно для того чтобы компьютер понимал что мы вводим число
my_age = my_age + 1             # Прибавляю к переменной еденицу

print("Ваш возвраст: " + str(my_age))           # Вывожу надпись "Ваш возраст" с значением переменной. Str используется для того чтобы поменять формат с числогого на строку, это нужно для того чтобы команда print вывела числа так как сама не умеет выводить ничего кроме строк