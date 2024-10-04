import sys


def main():
    # Памятка об использовании программы
    if len(sys.argv) != 3:
        print("Usage: python script.py <n_data> <m_data>")
        return
    # Присовение переменным значений аргументов
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_array_path(n, m)
    print(f"Пройденный путь: {result}")


def circular_array_path(n, m):
    # Создание массива
    circular_array = list(range(1, n + 1))

    # Создание переменных для записи и отслеживания пути
    path = []
    start_index = 0

    while True:
        # Добавление стартового элемента в начало массива пути
        path.append(circular_array[start_index])

        # Вычисление нового "стартового" индекса
        start_index = (start_index + m - 1) % n

        # Выход из цикла если вернулись на начальный элемент
        if start_index == 0:
            break

    return path


if __name__ == "__main__":
    main()
