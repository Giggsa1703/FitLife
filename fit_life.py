user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет? "))

#Рост, вес
user_weight = float(input("Введите ваш вес в кг: "))
user_height = float(input("Введите ваш рост в метрах: "))

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

#Расчет кол-ва воды
water_ml = user_weight * 30
water_l = water_ml / 1000

print(f"Привет, {user_name}! Твой возраст {user_age}.")
print(f"Твой индекс Массы Тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")

print("Расчет окончен. Будьте здоровы!")