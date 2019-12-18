# ! python3
# filling_in_the_gaps_challenge - inserts gaps into numbered files so that a new file can be added


import os
import re


prefix = input('Enter a prefix of files in which you want to have an inserted gap: ')
gap_number = input('Enter an index where you want to add a new file: ')
file_pattern = re.compile(prefix + r'(\d*)(\.\w+)')

get_path = input('Enter path to a folder: ')
files_list = os.listdir(get_path)

# removes unnecessary files from list
for file in files_list:
    if not (file.startswith(prefix) and os.path.isfile(os.path.join(get_path, file))):
        files_list.remove(file)

# making reversed lists which will be useful for later renaming
files_string = ' '.join(files_list)
matches = file_pattern.findall(files_string)
matches.reverse()
new_files_list = files_list[files_list.index(prefix + gap_number + matches[0][1]):]
new_files_list.reverse()

i = 0

# inserting gap
for file in new_files_list:
    new_number = str(int(matches[i][0]) + 1)
    if len(new_number) != len(matches[i][0]):
        new_number = '0' * (len(matches[i][0]) - len(new_number)) + new_number
    new_file = prefix + new_number + matches[i][1]
    os.rename(os.path.join(get_path, file), os.path.join(get_path, new_file))
    i += 1
