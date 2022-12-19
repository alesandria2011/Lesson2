#Человек вводит день и месяц своего рождения,выведите кем он является по знаку зодиака

a = int(input("Введите число вашего рождения: "))
b = int(input("Введите месяц вашего рождения: "))

if a >= 21 and a <= 31 and b == 3 or a >= 1 and a <= 20 and b == 4:
    print("Овен")
elif a >= 21 and a <= 30 and b == 4 or a >= 1 and a <= 21 and b == 5:
    print("Телец")
elif a >= 22 and a <= 31 and b == 5 or a >= 1 and a <= 21 and b == 6:
    print("Близнецы")
elif a >= 22 and a <= 30 and b == 6 or a >= 1 and a <= 22 and b == 7:
    print("Рак")
elif a >= 23 and a <= 31 and b == 7 or a >= 1 and a <= 23 and b == 8:
    print("Лев")
elif a >= 24 and a <= 31 and b == 8 or a >= 1 and a <= 23 and b == 9:
    print("Дева")
elif a >= 24 and a <= 30 and b == 9 or a >= 1 and a <= 23 and b == 10:
    print("Весы")
elif a >= 24 and a <= 31 and b == 10 or a >= 1 and a <= 22 and b == 11:
    print("Скорпион")
elif a >= 23 and a <= 30 and b == 11 or a >= 1 and a <= 21 and b == 12:
    print("Стрелец")
elif a >= 22 and a <= 31 and b == 12 or a >= 1 and a <= 20 and b == 1:
    print("Козерог")
elif a >= 21 and a <= 31 and b == 1 or a >= 1 and a <= 18 and b == 2:
    print("Водолей")
elif a >= 19 and a <= 29 and b == 2 or a >= 1 and a <= 20 and b == 3:
    print("Рыбы")
else:
    print("Введите число")






























