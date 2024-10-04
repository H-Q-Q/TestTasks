import json
import sys


def update_values(tests, values_map):
    # Рекурсивная функция для заполнения поля value в tests
    for test in tests:
        test_id = test.get('id')
        if test_id in values_map:
            test['value'] = values_map[test_id]
        if 'values' in test:
            update_values(test['values'], values_map)


def main(tests_path, values_path, report_path):
    # Чтение файлов
    with open(tests_path, 'r', encoding='utf-8') as f:
        tests_data = json.load(f)

    with open(values_path, 'r', encoding='utf-8') as f:
        values_data = json.load(f)

    # Преобразование values.json в словарь, для более удобной работы с данными
    values_map = {item['id']: item['value'] for item in values_data['values']}

    # Заполнение значений в tests.json на основании values.json
    update_values(tests_data['tests'], values_map)

    # Запись результата
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(tests_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Памятка об использовании программы
    if len(sys.argv) != 4:
        print("Usage: python script.py <tests.json> <values.json> <report.json>")
        sys.exit(1)

    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    report_path = sys.argv[3]

    main(tests_path, values_path, report_path)
