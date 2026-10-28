````markdown
# Система кэширования результатов операций с матрицами

Учебный проект по ПМ.06 «Сопровождение информационных систем» (учебная практика).

Программа предназначена для хранения результатов операций над матрицами в кэше. Для каждой пары матриц вычисляется уникальный хеш, позволяющий быстро находить ранее полученные результаты и избегать повторных вычислений.

## Установка

Программу устанавливать не нужно — достаточно, чтобы на компьютере был установлен Python 3 и находилась папка проекта.

1. Если Python 3 не установлен, скачайте его с сайта https://www.python.org/downloads/ и установите.
2. Проверьте, что Python работает:

```bash
python --version
```

3. Скачайте папку проекта с GitHub (зелёная кнопка Code → Download ZIP) и распакуйте её в любое место.

## Как запустить

Сторонние библиотеки не используются. Откройте командную строку в папке проекта и выполните:

```bash
python main.py
```

## Как пользоваться

Программа показывает меню:

1. Загрузить матрицы из файлов и выполнить операцию.
2. Просмотреть содержимое кэша.
3. Очистить кэш.
4. Создать резервную копию кэша.
5. Восстановить кэш из последней резервной копии.
0. Выход.

## Проверка тестами

```bash
python tests.py
```

Все тесты должны пройти (сообщение «Все тесты пройдены!»).

## Файлы проекта

| Файл | Назначение |
|------|------------|
| `main.py` | основная программа |
| `cache_manager.py` | модуль кэширования и хеширования матриц |
| `backup_manager.py` | резервное копирование и восстановление кэша |
| `io_handler.py` | модуль ввода-вывода (консоль и файлы) |
| `tests.py` | тесты |
| `matrix_A.txt` | пример входного файла для матрицы A |
| `matrix_B.txt` | пример входного файла для матрицы B |
| `ТЗ.md` | техническое задание |
| `README_ru.md` | руководство пользователя (русский язык) |
| `README_en.md` | руководство пользователя (английский язык) |
| `Регламент_ТО.md` | регламент технического обслуживания |

Автор: Орлова Анна Игоревна, группа ИСП-31, 3 курс.

Версия программы: 1.0

---

# Matrix Operations Cache System

Educational project for PM.06 "Information Systems Support" (internship).

The program is designed to store the results of matrix operations in a cache. A unique hash is calculated for each pair of matrices, allowing previously computed results to be found quickly and avoiding repeated calculations.

## Installation

The program does not require installation. You only need Python 3 and the project folder.

1. If Python 3 is not installed, download it from https://www.python.org/downloads/ and install it.
2. Check that Python works:

```bash
python --version
```

3. Download the project folder from GitHub (green **Code** button → **Download ZIP**) and extract it to any location.

## How to Run

No third-party libraries are required. Open a terminal in the project folder and run:

```bash
python main.py
```

## How to Use

The program displays a menu:

1. Load matrices from files and perform an operation.
2. View cache contents.
3. Clear the cache.
4. Create a backup copy of the cache.
5. Restore the cache from the latest backup.
0. Exit.

## Tests

```bash
python tests.py
```

All tests should pass (the message "All tests passed!" will be displayed).

## Project Files

| File | Purpose |
|------|---------|
| `main.py` | main program |
| `cache_manager.py` | caching and matrix hashing module |
| `backup_manager.py` | backup and restore of the cache |
| `io_handler.py` | input/output module (console and files) |
| `tests.py` | tests |
| `matrix_A.txt` | example input file for matrix A |
| `matrix_B.txt` | example input file for matrix B |
| `ТЗ.md` | technical specification (in Russian) |
| `README_ru.md` | user guide (Russian) |
| `README_en.md` | user guide (English) |
| `Регламент_ТО.md` | maintenance regulations (in Russian) |

Author: Orlova Anna Igorevna, group ISP-31, 3rd year.

Program version: 1.0
````
