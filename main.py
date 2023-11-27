#1
n = int(input("Введіть ціле число n: "))
print(n >= 100)

#2
# Введення двох дійсних чисел від користувача
num1 = float(input("Введіть перше дійсне число: "))
num2 = float(input("Введіть друге дійсне число: "))

# Визначення найбільшого числа за допомогою конструкції if-else
if num1 > num2:
    print(f"{num1} є більшим числом.")
elif num1 < num2:
    print(f"{num2} є більшим числом.")
else:
    print("Введені числа рівні.")

#3
# Введення рядка від користувача
user_input = input("Введіть рядок: ")

# Перевірка введеного рядка та виведення відповідного повідомлення
if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif user_input.lower() == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {user_input}!")

#4
# Введення з користувацьким значенням
income = float(input("Enter the annual income: "))

# Обчислення податку
tax = 0

if income > 0:
    if income <= 85528:
        tax = income * 0.18 - 556.02
    else:
        tax = 14839.02 + 0.32 * (income - 85528)

# Округлення до повних талерів
tax = round(max(tax, 0), 0)

# Виведення результату
print("The tax is:", tax, "thalers")

#5
# Введення номера року
year = int(input("Enter a year: "))

# Перевірка чи належить рік до григоріанської ери
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Визначення, чи є рік високосним чи звичайним
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

#6
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Просимо користувача ввести ціле число
user_number = int(input("Your guess: "))

# Використовуємо цикл while для перевірки введеного числа
while user_number != secret_number:
    # Якщо число не співпадає, виводимо повідомлення та просимо ввести ще раз
    print("Ha-ha! You're stuck in my loop!")
    user_number = int(input("Your guess: "))

# Якщо користувач вгадав число, виводимо відповідне повідомлення
print("Well done, muggle! You are free now.")

#7
import time

# Напишіть цикл for, який лічить до п'яти.
for i in range(1, 6):
    # Тіло циклу - виведення номеру ітерації циклу та слова "Міссісіпі".
    print(f"{i} Міссісіпі")
    # Тіло циклу - використання: time.sleep(1)
    time.sleep(1)

# Виведення фінального повідомлення.
print("Готовий чи ні, ось я!")

#8
# Використовуємо цикл while для безперервного запиту слів від користувача.
while True:
    # Просимо користувача ввести слово.
    user_input = input("Введіть слово: ")

    # Перевіряємо, чи введене слово є "chupacabra".
    if user_input.lower() == "chupacabra":
        # Якщо так, виводимо повідомлення та виходимо з циклу за допомогою break.
        print("You've successfully left the loop.")
        break

#9
# Просимо користувача ввести слово та присвоюємо його змінній user_word.
user_word = input("Введіть слово: ")

# Перетворюємо введене слово у верхній регістр.
user_word = user_word.upper()

# Проходимо по кожній літері у слові.
for letter in user_word:
    # Використовуємо умовне виконання та оператор continue для пропуску голосних.
    if letter in "AEIOU":
        continue
    # Виводимо на екран нез'їдені літери.
    print(letter)

#10
word_without_vowels = ""

# Просимо користувача ввести слово та присвоюємо його змінній user_word.
user_word = input("Введіть слово: ")

# Перетворюємо введене слово у верхній регістр.
user_word = user_word.upper()

# Проходимо по кожній літері у слові.
for letter in user_word:
    # Використовуємо умовне виконання та оператор continue для пропуску голосних.
    if letter in "AEIOU":
        continue
    # Додаємо нез'їдені літери до рядка word_without_vowels.
    word_without_vowels += letter

# Виводимо слово без голосних на екран.
print(word_without_vowels)

#11
blocks = int(input("Enter the number of blocks: "))

height = 0
blocks_needed = 0

while blocks_needed <= blocks:
    height += 1
    blocks_needed += height

height -= 1  # Віднімаємо 1, оскільки цикл завершується, коли blocks_needed стає більше blocks

print("The height of the pyramid:", height)

#12
def collatz_steps(num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(num)
        steps += 1
    return steps

# Зчитуємо введене користувачем число
user_input = int(input("Enter a natural number: "))

# Виводимо послідовність та кількість кроків
total_steps = collatz_steps(user_input)
print("steps =", total_steps)