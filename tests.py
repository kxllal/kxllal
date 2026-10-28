# Автоматические тесты для программы умножения матриц.
# Используются pytest и Faker.
#
# Установка:
# pip install pytest faker
#
# Запуск:
# pytest tests.py -v
# или
# python tests.py

import sys
import pytest
from faker import Faker

import main
import cache_manager
import backup_manager

fake = Faker("ru_RU")
fake.seed_instance(13)

def test_matrix_multiplication_2x2():
    """Тест 1: умножение матриц 2x2."""

    a = [
        [1, 2],
        [3, 4]
    ]

    b = [
        [5, 6],
        [7, 8]
    ]

    expected = [
        [19, 22],
        [43, 50]
    ]

    assert main.multiply_matrices(a, b) == expected

def test_identity_matrix():
    """Тест 2: умножение на единичную матрицу."""

    a = [
        [2, 3],
        [4, 5]
    ]

    identity = [
        [1, 0],
        [0, 1]
    ]

    assert main.multiply_matrices(a, identity) == a

def test_zero_matrix():
    """Тест 3: умножение на нулевую матрицу."""

    a = [
        [2, 4],
        [6, 8]
    ]

    zero = [
        [0, 0],
        [0, 0]
    ]

    expected = [
        [0, 0],
        [0, 0]
    ]

    assert main.multiply_matrices(a, zero) == expected

def test_random_matrices_size():
    """Тест 4: размер результата соответствует N×N."""

    n = fake.random_int(min=2, max=6)

    a = [[1] * n for _ in range(n)]
    b = [[1] * n for _ in range(n)]

    result = main.multiply_matrices(a, b)

    assert len(result) == n

    for row in result:
        assert len(row) == n

def test_hash_same_matrices():
    """Тест 5: одинаковые матрицы дают одинаковый хеш."""

    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    hash1 = cache_manager.create_hash(a, b)
    hash2 = cache_manager.create_hash(a, b)

    assert hash1 == hash2

def test_hash_different_matrices():
    """Тест 6: разные матрицы дают разные хеши."""

    a1 = [[1, 2], [3, 4]]
    b1 = [[5, 6], [7, 8]]

    a2 = [[9, 9], [9, 9]]
    b2 = [[1, 1], [1, 1]]

    hash1 = cache_manager.create_hash(a1, b1)
    hash2 = cache_manager.create_hash(a2, b2)

    assert hash1 != hash2

def test_cache_save_and_read(tmp_path, monkeypatch):
    """Тест 7: запись и чтение кэша."""

    cache_file = tmp_path / "cache.txt"

    monkeypatch.setattr(
        cache_manager,
        "CACHE_FILE",
        str(cache_file)
    )

    matrix_hash = "abc123"

    result = [
        [1, 2],
        [3, 4]
    ]

    cache_manager.save_cache(
        matrix_hash,
        result
    )

    restored = cache_manager.get_cache(
        matrix_hash
    )

    assert restored == result

def test_cache_missing_hash():
    """Тест 8: отсутствующий хеш возвращает None."""

    result = cache_manager.get_cache(
        "missing_hash"
    )

    assert result is None

def test_backup_creation(tmp_path, monkeypatch):
    """Тест 9: создание резервной копии."""

    cache_file = tmp_path / "cache.txt"
    backup_dir = tmp_path / "backup"

    cache_file.write_text(
        "test cache",
        encoding="utf-8"
    )

    monkeypatch.setattr(
        backup_manager,
        "CACHE_FILE",
        str(cache_file)
    )

    monkeypatch.setattr(
        backup_manager,
        "BACKUP_DIR",
        str(backup_dir)
    )

    backup_manager.make_backup()

    assert backup_dir.exists()

    assert len(list(backup_dir.iterdir())) == 1

def test_backup_restore(tmp_path, monkeypatch):
    """Тест 10: восстановление из копии."""

    cache_file = tmp_path / "cache.txt"
    backup_dir = tmp_path / "backup"

    cache_file.write_text(
        "correct data",
        encoding="utf-8"
    )

    monkeypatch.setattr(
        backup_manager,
        "CACHE_FILE",
        str(cache_file)
    )

    monkeypatch.setattr(
        backup_manager,
        "BACKUP_DIR",
        str(backup_dir)
    )

    backup_manager.make_backup()

    cache_file.write_text(
        "broken data",
        encoding="utf-8"
    )

    backup_manager.restore_backup()

    assert (
        cache_file.read_text(
            encoding="utf-8"
        )
        == "correct data"


)

def test_matrix_to_text():
    """Тест 11: преобразование матрицы в текст."""

    matrix = [
        [1, 2],
        [3, 4]
    ]

    text = main.matrix_to_text(matrix)

    assert "1 2" in text
    assert "3 4" in text

def test_random_matrix_values():
    """Тест 12: результат содержит только числа."""

    n = 3

    a = [
        [fake.random_int(0, 10) for _ in range(n)]
        for _ in range(n)
    ]

    b = [
        [fake.random_int(0, 10) for _ in range(n)]
        for _ in range(n)
    ]

    result = main.multiply_matrices(a, b)

    for row in result:
        for value in row:
            assert isinstance(value, int)

if __name__ == "__main__":
    print("Запуск тестов через pytest...")
    sys.exit(
        pytest.main(
            ["-v", __file__]
        )
    )
