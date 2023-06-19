import os


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


if __name__ == '__main__':
    print(get_subfolder_paths('d:\\'))
