import os


def sort(path):
    """
    данная функия сортирует файлы по папкам, критерием сортировки выступает расширение файла
    :param path: путь к папке которую надо отсортировать
    :return: вывод пустой
    """
    pass


def normalize(name):
    """
    данная функция нормализует название файла: приводит транслитерацию кириллического алфавита на латинский b аменяет все символы кроме латинских букв, цифр на '_'.
    :param name: название файла
    :return: возвращает нормализированное название файла
    """
    # транслитирация имени файла
    # замена всех символов кроме латинских и цифр на символ '_'
    # регистр букв остается таким каким был


def create_folder(path: str, name_dir: str):
    """
    создание папки для сортировки
    :param path:
    :param name_dir:
    :return:
    """
    new_dir = f"{path}/{name_dir}"
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)


def generate_folder_name(extension: str) -> str:
    """
    создание имени папки на основании расширения файла
    :param extension: расширение файл
    :return: имя папки
    """
    match_dict = {
        'image': ('JPEG', 'PNG', 'JPG', 'SVG'),
        'video': ('AVI', 'MP4', 'MOV', 'MKV'),
        'document': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
        'music': ('MP3', 'OGG', 'WAV', 'AMR'),
        'arch': ('ZIP', 'GZ', 'TAR'),
    }

    for key, valye in match_dict.items():
        if extension.upper() in valye:
            return key

    return 'no_name'


if name == 'main':




"""
    1) нормализируем названия файлов в папке
    2) создаем папки
    3) по расширению файла - переносим файлы в папки
"""