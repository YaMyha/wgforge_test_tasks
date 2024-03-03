def upload():
    file_path = 'b_numbers.txt'

    try:
        with open(file_path, 'r') as file:
            data = [line.strip() for line in file]
            return data
            print("Загружено!")
    except FileNotFoundError:
        print(f"Файл по пути '{file_path}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


def b(s):
    n, m = map(int, s[0].split())

    vehicles = []
    [vehicles.extend([list(map(int, i.split(","))) for i in s[nation+1].split()]) for nation in range(n)]
    sorted_array = sorted(vehicles, key=lambda x: (x[1], x[0]))
    print(*[item[0] for item in sorted_array][:30])


def b_simple():
    n, m = map(int, input().split())

    vehicles = []
    [vehicles.extend([list(map(int, i.split(","))) for i in input().split()]) for nation in range(n)]
    sorted_array = sorted(vehicles, key=lambda x: (x[1], x[0]))
    print(*[item[0] for item in sorted_array])

b_simple()