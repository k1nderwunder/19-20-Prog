import random
import string
from typing import List, Tuple

# Чистая функция для генерации случайного текста
def generate_random_text() -> str:
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(20)]
    return ' '.join(words)

# Чистая функция для поиска палиндромов
def find_palindromes(text: str) -> List[str]:
    words = ''.join(char if char.isalnum() else ' ' for char in text).split()
    return [word for word in words if word == word[::-1]]

# Чистая функция для печати палиндромов
def print_palindromes(palindromes: List[str]) -> None:
    print("Найденные палиндромы:")
    for palindrome in palindromes:
        print(palindrome)

# Чистая функция для ввода данных
def input_data() -> str:
    print("Выберите способ ввода данных:")
    print("1. Ввести данные вручную")
    print("2. Сгенерировать данные случайным образом")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        return input("Введите текст: ")
    elif choice == '2':
        return generate_random_text()
    else:
        print("Неверный выбор. Попробуйте снова.")
        return input_data()

# Функция высшего порядка для обработки меню
def process_menu(choice: str, state: Tuple[str, List[str], bool]) -> Tuple[str, List[str], bool]:
    text, palindromes, algorithm_executed = state

    if choice == '1':
        return input_data(), [], False
    elif choice == '2':
        if text:
            return text, find_palindromes(text), True
        else:
            print("Сначала введите данные.")
            return text, palindromes, algorithm_executed
    elif choice == '3':
        if algorithm_executed:
            if palindromes:
                print_palindromes(palindromes)
            else:
                print("Палиндромы не найдены.")
        else:
            print("Сначала выполните алгоритм.")
        return text, palindromes, algorithm_executed
    elif choice == '4':
        exit_program()
    else:
        print("Неверный выбор. Попробуйте снова.")
        return text, palindromes, algorithm_executed

# Чистая функция для завершения программы
def exit_program() -> None:
    print("Программа завершена.")
    exit()

def main() -> None:
    state = ("", [], False)

    while True:
        print("Меню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")
        state = process_menu(choice, state)

if __name__ == "__main__":
    main()