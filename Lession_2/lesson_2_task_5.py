number_mounth = int(input('Введите номер месяца: '))

def month_to_season(number_mounth):
    if (number_mounth == 1 or number_mounth == 2 or number_mounth == 12):
        return "Зима"
    elif (number_mounth == 3 or number_mounth == 4 or number_mounth == 5):
        return "Весна"
    elif (number_mounth == 6 or number_mounth == 7 or number_mounth == 8):
        return "Лето"
    elif (number_mounth == 9 or number_mounth == 10 or number_mounth == 11):
        return "Осень"
    else:
        return("Укажите корректный номер месяца")
    
print(month_to_season(number_mounth))