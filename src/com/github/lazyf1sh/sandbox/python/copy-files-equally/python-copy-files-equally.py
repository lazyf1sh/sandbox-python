
import glob
import os
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def get_list_files(folder_path, resursive):
    return glob.glob(folder_path + "/**", recursive=resursive)


def create_dirs(catalog_path):
    if not os.path.exists(catalog_path):
        try:
            print("creating dir: ", catalog_path)
            os.makedirs(catalog_path)
            print("dir created: ", catalog_path)
            return True
        except FileExistsError as e:
            print(e)


source_path = "/media/qwerty/touro-2/traum_books_for_mum_using_flash/pool_to_take_from/"
target_path = "/media/qwerty/5CAE-5C36/"

letters = get_list_files(source_path, False)

for letter in letters:
    current_letter = letter.split('/')[len(letter.split('/')) - 1]
    if current_letter == "О":
        continue
    letter_folders = get_list_files(letter, False)
    files_per_target_folder = len(letter_folders) / 50
    target_folder_counter = 0
    current_file_in_a_folder = 0
    for letter_folder in letter_folders:
        if files_per_target_folder <= current_file_in_a_folder:
            current_file_in_a_folder = 0
            target_folder_counter += 1
        target_folder_name = letter_folder.split('/')[len(letter_folder.split('/')) - 1]
        target_folder = target_path + current_letter + "/" + format(target_folder_counter, "03") + "/" + target_folder_name
        create_dirs(target_folder)
        copytree(letter_folder, target_folder)
        current_file_in_a_folder += 1
