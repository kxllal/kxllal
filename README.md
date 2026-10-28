Умножение матриц $N \times N$ с кэшированием результатов

Учебный проект по ПМ.06 «Сопровождение информационных систем» (учебная практика).
Программа на Python находит произведение двух квадратных матриц $A \times B$ размером $N \times N$. Элементы матриц и размерность $N$ задаются пользователем. Реализовано кэширование результатов для исключения повторных вычислений.

Математическая основа:
Для матриц $A$ и $B$ размерности $N \times N$ элемент результирующей матрицы $C$ вычисляется по формуле:
$C_{ij} = \sum_{k=1}^{N} A_{ik} \cdot B_{kj}$

Установка

Программу устанавливать не нужно — достаточно, чтобы на компьютере стоял Python 3 и была папка проекта.

Если Python 3 не установлен, скачайте его с сайта https://www.python.org/downloads и установите.
Проверьте, что Python работает:
Копировать
python --version
Скачайте папку проекта с GitHub (зелёная кнопка Code → Download ZIP) и распакуйте её в любое место.
Как запустить

Сторонние библиотеки не используются (используется только стандартная библиотека Python). Откройте командную строку в папке проекта и выполните:

Копировать
python main.py
Как пользоваться

Программа показывает меню:

Ввод с клавиатуры — вводим $N$ и элементы матриц, результат выводится на экран.
Работа с файлами — $N$ и матрицы читаются из файлов matrix_A.txt и matrix_B.txt, результат записывается в result.txt.
Показать реестр кэша — вывести список всех сохраненных вычислений (файл cache_registry.json).
Сделать резервную копию кэша — создать архив папки cache (папка backup).
Восстановить кэш из копии — вернуть состояние кэша из последней резервной копии.
Выход.
Проверка тестами
Копировать
python tests.py

Все тесты должны пройти (сообщение «Все тесты пройдены!»).

Файлы проекта
Файл	Назначение
main.py	основная программа (точка входа)
matrix_core.py	модуль умножения матриц и валидации
cache_manager.py	модуль кэширования и хеширования матриц
backup_manager.py	резервное копирование и восстановление кэша
io_handler.py	модуль ввода-вывода (консоль и файлы)
tests.py	тесты
matrix_A.txt	пример файла для ввода матрицы A
matrix_B.txt	пример файла для ввода матрицы B
ТЗ.md	техническое задание
README_ru.md	руководство пользователя (русский)
README_en.md	руководство пользователя (английский)
Регламент_ТО.md	регламент технического обслуживания

Автор: [Орлова Анна Игоревна], группа [ИСП-31], [3].

Версия программы: 1.0

Matrix Multiplication $N \times N$ with Result Caching

Educational project for PM.06 "Information Systems Support" (internship).
A Python program that finds the product of two square matrices $A \times B$ of size $N \times N$. Matrix elements and dimension $N$ are entered by the user. Result caching is implemented to avoid redundant calculations.

Mathematical basis:
For matrices $A$ and $B$ of size $N \times N$, the element of the resulting matrix $C$ is calculated as:
$C_{ij} = \sum_{k=1}^{N} A_{ik} \cdot B_{kj}$

Installation

The program does not need to be installed — you only need Python 3 and the project folder.

If Python 3 is not installed, download it from https://www.python.org/downloads and install it.
Check that Python works:
Копировать
python --version
Download the project folder from GitHub (green Code button → Download ZIP) and unpack it anywhere.
How to run

No third-party libraries are used (only Python Standard Library). Open a terminal in the project folder and run:

Копировать
python main.py
How to use

The program shows a menu:

Keyboard input — enter $N$ and matrix elements, the result is printed on the screen.
File mode — $N$ and matrices are read from matrix_A.txt and matrix_B.txt, the result is written to result.txt.
Show cache registry — display the list of all saved computations (file cache_registry.json).
Make cache backup — create an archive of the cache folder (folder backup).
Restore cache from backup — revert the cache state from the latest backup.
Exit.
Tests
Копировать
python tests.py

All tests must pass (the message "All tests passed!").

Project files
File	Purpose
main.py	main program (entry point)
matrix_core.py	matrix multiplication and validation module
cache_manager.py	caching and matrix hashing module
backup_manager.py	backup and restore of the cache
io_handler.py	I/O module (console and files)
tests.py	tests
matrix_A.txt	example input file for matrix A
matrix_B.txt	example input file for matrix B
ТЗ.md	technical specification (in Russian)
README_ru.md	user guide (Russian)
README_en.md	user guide (English)
Регламент_ТО.md	maintenance regulations (in Russian)

Author: [Orlova Anna Igorevna], group [ISP‑31], [3].

Program version: 1.0
