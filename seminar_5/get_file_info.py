"""Напишите функцию get_file_info, которая принимает на вход строку -
абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
путь, имя файла, расширение файла.
file_path = 'C:/Users/User/Documents/example.txt'
file_path = '/home/user/data/file.py'
file_path = 'D:/myfile.txt'
file_path = 'C:/Projects/project1/code/script.py'
file_path = '/home/user/docs/my.file.with.dots.txt'
file_path = 'file_in_current_directory.txt'"""

from pathlib import Path
import os


def get_file_info(file_path: str):
    """принимает на вход строку - абсолютный путь до файла.
    Функция возвращает кортеж из трёх элементов: 
    путь, имя файла, расширение файла."""
    file = Path(file_path)
    if dir_path := os.path.dirname(file):
        dir_path = dir_path.replace('\\', '/')
        if dir_path[-1] != '/':
            dir_path += '/'

    return (dir_path, file.stem, file.suffix, )


file_path: str = '/home/user/docs/my.file.with.dots.txt'
print(get_file_info(file_path))
