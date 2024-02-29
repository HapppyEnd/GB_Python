"""Напишите функцию группового переименования файлов в папке test_folder
под названием rename_files. Она должна:
a. принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно
работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для
диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним
прибавляется желаемое конечное имя, если оно передано. Далее счётчик
файлов и расширение.
f. Папка test_folder доступна из текущей директории

"""
import os
from pathlib import Path


def rename_files(desired_name, num_digits, source_ext, target_ext):
    """Group renema files."""
    folder_path = Path('test_folder')
    if not Path(folder_path).is_dir():
        folder_path.mkdir(parents=True)

    files = os.listdir(folder_path)
    print(files)
    file_counter = 1

    for file in files:
        # Убедиться, что файл имеет нужное расширение
        if file.endswith('.' + source_ext):
            # Получить диапазон из оригинального имени файла
            original_name_range = file[3:6]
            # Сгенерировать порядковый номер файла
            file_number = str(file_counter).zfill(num_digits)
            # Составить новое имя файла
            new_file_name = desired_name + file_number + "." + target_ext
            # Полный путь к исходному файлу
            source_file_path = os.path.join(folder_path, file)
            # Полный путь к новому файлу
            target_file_path = os.path.join(folder_path, new_file_name)
            # Переименовать файл
            os.rename(source_file_path, target_file_path)
            file_counter += 1
