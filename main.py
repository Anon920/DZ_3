# Умовні конструкції
print("Перевірка паролю")
user_password = input('Введіть ваш пароль: ')

if user_password == 'password123':
    print('Ви увійшли в систему')
else:
    print("Неправильний пароль")

print("Визначення днів тижня")

days_of_week = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}

day_number = int(input("Введіть номер дня тижня(1-7): "))

if 1 <= day_number <= 7:
    print(days_of_week[day_number])
else:
    print("Помилка: недійсний номер дня. Введіть число від 1 до 7.")

# Цикли

print("Таблиця множення")

number = int(input("Введіть число для таблиці множення: "))

print(f"Таблиця множення для числа {number}:")
for i in range(1, 11):
    print(f"{i} * {number} = {i*number}")

print("Сума чисел")

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = sum(numbers)

print(sum_of_numbers)

print("Факторіал числа")

number = int(input("Введіть число для обчислення факторіалу: "))

factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
print(f"Результат обчилення факторіалу: {factorial}")

print("Парні числа")

for i in range(2, 51, 2):
    print(i)

print("Пошук простих чисел")

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

number_list = []

for i in range(start, end + 1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        number_list.append(i)

print(f"Прості числа в діапазоні від {start} до {end}: {number_list}")
