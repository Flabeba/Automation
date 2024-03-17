side_square = input("Введите сторону квадрата: ")
side_square = int(side_square)
round(side_square)          # Округляет число до целого вверх

def square(side_square):
    square_area = pow(side_square, 2)           # pow возведение в степень
    return square_area 

launch_calc = square(side_square)

print("Площадь квадрата равна: " + str(launch_calc))