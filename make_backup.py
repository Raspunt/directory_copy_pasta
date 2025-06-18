#!/bin/python3

import subprocess
import os
import sys
from datetime import datetime

# Путь откуда копируем
source = "/"  # поменяй под себя

# Базовый путь куда копируем
base_destination = "/home/boxman/Downloads/"  # на втором диске

# Режим: True — каждый раз новая копия, False — всегда перезаписывать
archive_mode = True

# Создаём путь назначения
if archive_mode:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination = os.path.join(base_destination, f"backup_{timestamp}")
else:
    destination = os.path.join(base_destination, "latest")

# Проверки
if not os.path.exists(source):
    print(f"❌ Источник не найден: {source}")
    sys.exit(1)

os.makedirs(destination, exist_ok=True)

# Команда rsync
cmd = [
    "rsync",
    "-aAXv",          # права, ACL, xattr
    "--delete",       # удалять лишнее на стороне назначения
    "--human-readable",
    source + "/",     # важно: слэш чтобы копировать содержимое, а не сам каталог
    destination
]

print(f"📁 Копирование {source} → {destination}")
result = subprocess.run(cmd)

if result.returncode == 0:
    print("✅ Копирование завершено.")
else:
    print(f"❌ Ошибка, код: {result.returncode}")
