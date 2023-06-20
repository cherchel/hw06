import os


def sort(path):
    for filename in os.listdir(path):
        extension = os.path.splitext(filename)[1][1:]   # определение расширения
        folder_name = generate_folder_name(extension)   # создание название новой папки
        create_folder(path, folder_name)                # создание новой папки
        new_path = f"{path}{folder_name}"              # создание пути
        shutil.move(path, new_path)                     # перемещение файла в папку

    return
