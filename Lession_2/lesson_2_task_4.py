input_numper = input("Введите число: ")
input_numper = int(input_numper)

def fizz_buzz(input_numper):
    if ((input_numper % 5 == 0) and (input_numper % 3 == 0)):           # if это условие если. Если переменная без остатка делится на пять и без остатка делится на три, то возвращается физ бис
        return "FizzBuzz"
    elif (input_numper % 5 == 0):           # elif = Но если. Это исключение при котором выполняется другое условие
        return "Buzz"
    elif (input_numper % 3 == 0):
        return "Fizz"
    else:                                   # Если не выполняются другие условия
        return "Число не делится на 3 или 5"

print(fizz_buzz(input_numper))