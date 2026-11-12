#Calculator
parts = {
    1: ("Капот", 1.0),
    2: ("Передняя дверь", 1.2),
    3: ("Задняя дверь", 1.1),
    4: ("Передний бампер", 1.0),
    5: ("Задний бампер", 1.0),
    6: ("Крыша", 1.1),
}

colors = {
    1: ("Белый", 1.0),
    2: ("Синий", 1.0),
    3: ("Жёлтый", 1.1),
    4: ("Красный", 1.0),
    5: ("Перламутровый", 1.2),
    6: ("Серый металлик", 1.3),
}

print("Калькулятор стоимости покраски автомобиля")

print("\nДетали")
for number, (name, _) in parts.items():
    print(f"{number}. {name}")
part_number = int(input("Введите номер детали: "))

print("\nЦвета")
for number, (name, _) in colors.items():
    print(f"{number}. {name}")
color_number = int(input("Введите номер цвета: "))

part_coefficient = parts[part_number][1]
color_coefficient = colors[color_number][1]
price = 12000 * part_coefficient * color_coefficient

formatted_price = f"{price:,.0f}".replace(",", " ")
print(f"\nСтоимость покраски: {formatted_price} руб.")