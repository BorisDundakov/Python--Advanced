import os

dirpath, directories, files = next(os.walk(input()))

by_extension = {}
for file in files:
    extention = file.split('.')[-1]

    if extention not in by_extension:
        by_extension[extention] = []

    by_extension[extention].append(file)

with open(os.path.expanduser("~/Desktop/report.txt"), 'w') as output_file:
    for extention in sorted(by_extension):
        files = sorted(by_extension[extention])
        output_file.write(f'.{extention}\n')

    for file in files:
        output_file.write(f'---{file}\n')
# TODO - .py and .html files are not appearing
# TODO - file isn't generated on desktop
print(by_extension)
# успешно сме групирали файловете по extention type
