import random


def b_gen(n, m):
    file_name = 'b_numbers.txt'

    with open(file_name, 'w') as file:
        file.write(f"{n} {m}\n")
        for i in range(n):
            random_numbers = " ".join(
                [f"{random.randint(1, 10 ** 10)},{random.randint(1, 10)} " for _ in range(m)])
            if i != n - 1:
                file.write(random_numbers + "\n")
            else:
                file.write(random_numbers)
    print(f"Сгенерированные числа записаны в файл {file_name}.")

# b_gen(11, 30000)
def c_gen():
    # Генерация случайных чисел
    length = 10**4
    random_numbers = [random.randint(1, 10**8) for _ in range(length)]

    # Имя файла для записи
    file_name = 'numbers.txt'

    # Запись чисел в текстовый файл
    with open(file_name, 'w') as file:
        file.write(f"{length}\n")
        for number in random_numbers:
            file.write(f"{number} ")

    print(f"Сгенерированные числа записаны в файл {file_name}.")

c_gen()
