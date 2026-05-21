# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))

# 2. Сбор данных
user_weight = float(input("Введите ваш вес в кг: "))
user_height = float(input("Введите ваш рост в метрах: "))


# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


#Расчет кол-ва воды
water_ml = user_weight * 30
water_needed = water_ml / 1000


print(f"Привет, {user_name}! Твой возраст {user_age}.")
print(f"Твой индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")