# Резервное копирование и восстановление кэша матричных вычислений.
# Копия кэша сохраняется в папку backup, в имени файла указываются дата и время.
# Можно запустить отдельно: python backup_manager.py

import os
import shutil
import datetime

CACHE_FILE = "cache.txt"
BACKUP_DIR = "backup"

def make_backup():
    """Создание резервной копии кэша."""
    if not os.path.exists(CACHE_FILE):
        print("Файл кэша отсутствует, создавать копию нечего")
        return

    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = os.path.join(
        BACKUP_DIR,
        f"cache_{current_time}.txt"
    )

    shutil.copy(CACHE_FILE, backup_name)
    print("Резервная копия создана:", backup_name)

def restore_backup():
    """Восстановление кэша из последней резервной копии."""
    if not os.path.exists(BACKUP_DIR):
        print("Папка backup отсутствует, восстановление невозможно")
        return

    backups = os.listdir(BACKUP_DIR)

    if len(backups) == 0:
        print("Резервные копии отсутствуют")
        return

    backups.sort()
    latest_backup = backups[-1]

    shutil.copy(
        os.path.join(BACKUP_DIR, latest_backup),
        CACHE_FILE
    )

    print("Кэш восстановлен из копии:", latest_backup)

if __name__ == "__main__":
    print("1 - создать резервную копию кэша")
    print("2 - восстановить кэш из копии")

    choice = input("Выберите пункт: ").strip()

    if choice == "1":
        make_backup()
    elif choice == "2":
        restore_backup()
    else:
        print("Нет такого пункта меню")
