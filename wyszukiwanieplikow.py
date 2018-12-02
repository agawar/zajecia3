import os
import os.path

size_list = {}
def przegladanie(root):
    file_list = os.listdir(root)
    dir_list = []

    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)

            if file_size not in size_list:
                size_list[file_size] = [full_name]
            else:
                size_list[file_size].append(full_name)

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)

    for dirname in dir_list:
        przegladanie(os.path.join(root, dirname))

    return(size_list)

przegladanie(".")

for size in size_list:
    print("{0}: {1}".format(size, size_list[size]))
