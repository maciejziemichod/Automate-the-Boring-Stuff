# ! python3
# filling_in_the_gaps - finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single
# folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# The program renames all the later files to close this gap.


import re
import os

prefix = input('Enter a prefix of files you want to have properly numbered: ')
file_pattern = re.compile('(' + prefix + ')' + r'(\d*)(\.\w+)')

get_path = input('Enter path to a folder: ')
files_list = os.listdir(get_path)

for file in files_list:  # throws out everything which is not a file
    if not (file.startswith(prefix) and os.path.isfile(os.path.join(get_path, file))):
        files_list.remove(file)

files_string = ' '.join(files_list)
files_matching = file_pattern.findall(files_string)  # finds all the numbering

for file in files_matching:  # fixes numbering
    if int(file[1]) / (files_matching.index(file) + 1) != 1:
        new_number = str(files_matching.index(file) + 1)
        if len(new_number) != len(file[1]):
            new_number = '0' * (len(file[1]) - len(new_number)) + new_number
        os.rename(os.path.join(get_path, file[0] + file[1] + file[2]),
                  os.path.join(get_path, file[0] + new_number + file[2]))

print('Done')
