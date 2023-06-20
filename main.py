import os


def sort(path: str):
    """
    данная функия сортирует файлы по папкам, критерием сортировки выступает расширение файла
    :param path: путь к папке которую надо отсортировать
    :return:
    """
    for filename in os.listdir(path):
        extension = os.path.splitext(filename)[1][1:]   # определение расширения
        folder_name = generate_folder_name(extension)   # создание название новой папки
        create_folder(path, folder_name)                # создание новой папки

        old_path_file = f"{path}{filename}"
        new_path_file = f"{path}{folder_name}\\{filename}"
        os.replace(old_path_file, new_path_file)        # перемещение файла в новую папку

    return


def normalize(name: str):
    """
    данная функция нормализует название файла: приводит транслитерацию кириллического алфавита
    на латинский b аменяет все символы кроме латинских букв, цифр на '_'.
    :param name: название файла
    :return: возвращает нормализированное название файла
    """
    cyrillic_simbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ!\"#$%&'()*+,- "
    translation = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_",
        "_", "_", "_", "_", "_", "_", "_", "_", "_")

    trans = {}
    for c, t in zip(cyrillic_simbols, translation):
        trans[ord(c)] = t
        trans[ord(c.upper())] = t.upper()

    return name.translate(trans)


def rename_files(path: str):
    """
    функция переименовывает все файлы в указанной директории
    :param path: путь к директории
    :return:
    """
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            old_name = os.path.join(path, filename)
            new_name = os.path.join(path, normalize(filename))
            os.replace(old_name, new_name)


def create_folder(path: str, name_dir: str):
    """
    создание папки для сортировки
    :param path: директория в которой надо создать новую папку
    :param name_dir: название которое надо дать новой папке
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
        'document': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'XLS', 'PPTX'),
        'music': ('MP3', 'OGG', 'WAV', 'AMR'),
        'arch': ('ZIP', 'GZ', 'TAR'),
    }

    for key, valye in match_dict.items():
        if extension.upper() in valye:
            return key

    return 'no_name'


if __name__ == '__main__':
    path = input("Введи пусть к папке: ")
    rename_files(path)                      # все файлы в указанной папке - стандартизируются(нормализируются)
    sort(path)                              # происходит сортировка файлов по папкам согласно их расширениям
