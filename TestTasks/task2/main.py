import sys
import math


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x_c, y_c = map(float, file.readline().split())
        radius = float(file.readline())
    return x_c, y_c, radius


def read_points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_relative_to_circle(x_c, y_c, radius, x_p, y_p):
    # Функция используется для определения положения точки относительно окружностиэ
    distance = math.sqrt((x_p - x_c) ** 2 + (y_p - y_c) ** 2)
    if abs(distance - radius) < 1:  # Точка на окружности
        return 0
    elif distance < radius:  # Точка внутри окружности
        return 1
    else:  # Точка снаружи окружности
        return 2


def main():
    # Памятка об использовании программы
    if len(sys.argv) != 3:
        print("Usage: python script.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Чтение данных окружности и точек
    x_c, y_c, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    # Обработка каждой точки
    for x_p, y_p in points:
        result = point_relative_to_circle(x_c, y_c, radius, x_p, y_p)
        print(result)


if __name__ == "__main__":
    main()
