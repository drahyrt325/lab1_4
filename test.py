from lib import count_common_elements


def test_common_elements():
    """Тест 1: Обычные списки с общими элементами"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    # Общий элемент: 5
    result = count_common_elements(list1, list2, list3)
    assert result == 1, f"Ожидалось 1, получено {result}"
    print("✓ Тест 1 пройден: 1 общий элемент (5)")


def test_all_elements_same():
    """Тест 2: Все элементы одинаковые"""
    result = count_common_elements([1, 2], [1, 2], [1, 2])
    assert result == 2, f"Ожидалось 2, получено {result}"
    print("✓ Тест 2 пройден: 2 общих элемента")


def test_no_common_elements():
    """Тест 3: Нет общих элементов"""
    result = count_common_elements([1, 2], [3, 4])
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("✓ Тест 3 пройден: 0 общих элементов")


def test_single_list():
    """Тест 4: Один список - все элементы считаются общими"""
    result = count_common_elements([1, 2, 3])
    assert result == 3, f"Ожидалось 3, получено {result}"
    print("✓ Тест 4 пройден: в одном списке все 3 элемента")


def test_empty_lists():
    """Тест 5: Пустые списки"""
    result = count_common_elements([], [])
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("✓ Тест 5.1 пройден: два пустых списка")


def test_no_arguments():
    """Тест 6: Без аргументов"""
    result = count_common_elements()
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("✓ Тест 5.2 пройден: без аргументов")


def test_with_duplicates():
    """Тест 7: Списки с дубликатами"""
    result = count_common_elements([1, 1, 2, 2], [1, 2, 2, 3], [1, 1, 2])
    # Общие элементы: 1 и 2
    assert result == 2, f"Ожидалось 2, получено {result}"
    print("✓ Тест 7 пройден: 2 общих элемента с дубликатами")


def test_mixed_types():
    """Тест 8: Разные типы данных"""
    result = count_common_elements([1, 'a', True], ['a', True, 2], [True, 3, 'a'])
    # Общие: 'a' и True (True == 1, но в Python True != 1 в множествах)
    assert result == 2, f"Ожидалось 2, получено {result}"
    print("✓ Тест 8 пройден: разные типы данных")


if __name__ == "__main__":
    print("Запуск тестов для count_common_elements()\n")

    test_common_elements()
    test_all_elements_same()
    test_no_common_elements()
    test_single_list()
    test_empty_lists()
    test_no_arguments()
    test_with_duplicates()
    test_mixed_types()

    print("\n✅ Все тесты успешно пройдены!")