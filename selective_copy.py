#! python3
# selective_copy - walks through a folder tree and searches for files with a certain file extension.
# Then it copies these files from whatever location they are in to a new folder in CWD.

import os
import shutil


def search_files(path, extension):
    copy_folder = os.getcwd() + '\\' + str(extension)
    if not os.path.exists(copy_folder):
        os.mkdir(copy_folder)
    print('Files with given extension:')
    for foldername, subfolders, filenames in os.walk(os.path.abspath(path)):
        for filename in filenames:
            if filename.endswith(extension):
                file_path = foldername + '\\' + filename
                print(file_path)
                print('Copying ' + filename + ' to ' + copy_folder)
                shutil.copy(file_path, copy_folder)


path = input('Enter path to a folder: ')
extension = input('Enter extension you are looking for: ')
search_files(path, extension)
print('\n Done')
