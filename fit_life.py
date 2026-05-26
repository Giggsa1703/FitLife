#  Первый проект
# Знакомство с пользователем
user_name = input("Как тебя зовут? ")
user_age = int(input("Сколько тебе лет?(только цифры) "))


# Рост,вес
user_weight = float(input("Введите ваш вес в кг: (например 80) "))
user_height = float(input("Введите ваш рост в метрах: (например 1.75) "))


# Расчёт индекса
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)


# Расчёт кол-ва воды
ML = 30
KG = 1000
WATER_ML = user_weight * ML
WATER_L = WATER_ML / KG


if __name__ == '__main__':
    print(f"Привет, {user_name}! Твой возраст {user_age}.")
    print(f"Твой индекс Массы Тела: {bmi_rounded}")
    print(f"Рекомендуемая норма воды: {WATER_L:.1f} л. в день")

    print("Расчет окончен. Будьте здоровы!")
