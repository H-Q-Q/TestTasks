import sys


def min_moves_to_equal_elements(nums):
    # Сортировка массива, чтобы найти медиану
    nums.sort()
    n = len(nums)

    # Поиск медианы
    if n % 2 == 0:
        median = nums[n // 2 - 1]  # Медиана для четного количества
        print(median)
    else:
        median = nums[n // 2]  # Медиана для нечетного количества

    # Подсчёот ходов происходит путём подсчёта разности по модулю между каждым элементом массива и медианой
    moves = sum(abs(num - median) for num in nums)
    return moves


if __name__ == "__main__":
    # Памятка об использовании программы
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        nums = [int(line.strip()) for line in f.readlines()]

    result = min_moves_to_equal_elements(nums)
    print(result)
