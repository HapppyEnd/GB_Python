"""Из созданных на уроке и в рамках домашнего задания функций, соберите
пакет для работы с файлами.
Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory."""

with open('__init__.py', "w", encoding='utf-8') as init_file:
    init_file.write(
        '''def get_dir_size\ndef save_results_to_json\n
        def save_results_to_csv\ndef save_results_to_pickle\n
        def traverse_directory''')
