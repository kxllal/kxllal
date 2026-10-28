# Учебная практика ПМ.06.
# Программа находит произведение двух матриц размера N×N.
# Размерность и элементы матриц задаются пользователем.
# Результаты вычислений сохраняются в кэш для повторного использования.

import os
import logging
import datetime

import cache_manager
import backup_manager
import io_handler

CACHE_FILE = "cache.txt"

# --- ЖУРНАЛ РАБОТЫ -------------------------------------------------------

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    encoding="utf-8",
)

def time_now_text():
    # Текущие дата и время в текстовом формате.
    now = datetime.datetime.now()

    day = str(now.day).zfill(2)
    month = str(now.month).zfill(2)
    year = str(now.year)

    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)

    return (
        day + "." + month + "." + year +
        " " +
        hour + ":" + minute + ":" + second
    )

def multiply_matrices(matrix_a, matrix_b):
    # Вычисление произведения двух квадратных матриц.

    size = len(matrix_a)

    result = []

    for i in range(size):
        row = []

        for j in range(size):
            value = 0

            for k in range(size):
                value += matrix_a[i][k] * matrix_b[k][j]

            row.append(value)

        result.append(row)

    return result

def matrix_to_text(matrix):
    # Преобразование матрицы в текст для вывода.

    lines = []

    for row in matrix:
        lines.append(" ".join(map(str, row)))

    return "\n".join(lines)

def calculate_from_console():
    # Ввод матриц с клавиатуры.

    n = int(input("Введите размерность матриц N: "))

    print("Введите элементы матрицы A:")

    matrix_a = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix_a.append(row)

    print("Введите элементы матрицы B:")

    matrix_b = []

    for i in range(n):
        row = list(map(int, input().split()))
        matrix_b.append(row)

    matrix_hash = cache_manager.create_hash(
        matrix_a,
        matrix_b
    )

    cached_result = cache_manager.get_cache(
        matrix_hash
    )

    if cached_result is not None:
        print("Результат получен из кэша:")
        print(matrix_to_text(cached_result))

        logging.info(
            "Использован результат из кэша"
        )

        return

    result = multiply_matrices(
        matrix_a,
        matrix_b
    )

    cache_manager.save_cache(
        matrix_hash,
        result
    )

    print("Результат умножения:")

    print(matrix_to_text(result))

    logging.info(
        "Выполнено новое вычисление и сохранено в кэш"
    )

def calculate_from_files():
    # Чтение матриц из файлов.

    matrix_a = io_handler.read_matrix(
        "matrix_A.txt"
    )

    matrix_b = io_handler.read_matrix(
        "matrix_B.txt"
    )

    matrix_hash = cache_manager.create_hash(
        matrix_a,
        matrix_b
    )

    cached_result = cache_manager.get_cache(
        matrix_hash
    )

    if cached_result is not None:

        io_handler.write_matrix(
            "result.txt",
            cached_result
        )

        print(
            "Результат найден в кэше и записан в result.txt"
        )

        return

    result = multiply_matrices(
        matrix_a,
        matrix_b
    )

    cache_manager.save_cache(
        matrix_hash,
        result
    )

    io_handler.write_matrix(
        "result.txt",
        result
    )

    print(
        "Результат вычислен и записан в result.txt"
    )

def main():

    print(
        "Программа кэширования произведения матриц"
    )

    logging.info("Программа запущена")

    while True:

        print()
        print("1 - ввод матриц с клавиатуры")
        print("2 - чтение матриц из файлов")
        print("3 - показать содержимое кэша")
        print("4 - создать резервную копию кэша")
        print("5 - восстановить кэш из копии")
        print("0 - выход")

        choice = input(
            "Выберите пункт: "
        ).strip()

        logging.info(
            f"Выбран пункт меню: {choice}"
        )

        if choice == "1":
            calculate_from_console()

        elif choice == "2":
            try:
                calculate_from_files()
            except FileNotFoundError:
                print(
                    "Не найдены файлы matrix_A.txt или matrix_B.txt"
                )

        elif choice == "3":
            cache_manager.show_cache()

        elif choice == "4":
            backup_manager.make_backup()

        elif choice == "5":
            backup_manager.restore_backup()

        elif choice == "0":

            print(
                "Работа программы завершена"
            )

            logging.info(
                "Работа программы завершена"
            )

            break

        else:

            print(
                "Нет такого пункта меню"
            )

            logging.warning(
                f"Неверный пункт: {choice}"
            )

if __name__ == "__main__":
    main()
