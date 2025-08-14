# Напишите функцию, которая считает количество гласных в строке, и создайте тесты для этой функции.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for i, char in enumerate(s): # i - порядковый номер, char - буквенный символ
        if char in vowels:
            count += 1
        elif char.lower() == 'y' and i != 0: # Проверяем, является ли буква "y" первой в слове
            if s[i - 1] not in vowels and s[i - 1].lower() != 'y': # Проверяем, является ли буква перед буквой "y" гласной
                count += 1
    return count
