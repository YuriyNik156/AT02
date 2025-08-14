# Тесты для функции, которая считает количество гласных в слове

import pytest
from main_hw import count_vowels

# Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
def test_only_vowels():
    assert count_vowels('aeiou') == 5

# Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
def test_no_vowels():
    assert count_vowels('rhthm') == 0

# Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).
@pytest.mark.parametrize("test_input", "expected", [
    ("classic", 2),     # a, i
    ("GALLERY", 3),     # A, E, Y
    ("pythON", 2),      # y после p - гласная, O
    ("myth", 1),        # y после m - гласная
    ("yellow", 2),      # y в начале слова - не гласная, e, o
    ("boy", 1),         # y после o - не гласная, o
    ("layer", 2),       # a, y после a - не гласная, e
    ("", 0),            # пустая строка
    ("AEIOUaeiou", 10)  # все гласные
])

def test_mixed_letters(test_input, expected):
    assert count_vowels(test_input) == expected
