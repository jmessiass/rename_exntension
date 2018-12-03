import os


def main():
    path = os.getcwd()
    extension_from = input('Type current extension: (ex: .txt) ')
    extension_to = input('Type new extension: (ex: .html) ')
    count = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            if extension_from in file:
                dir_file = os.path.join(root, file)
                dir_file_new = dir_file.replace(extension_from, extension_to)
                os.rename(dir_file, dir_file_new)
                print('%s -> %s' % (dir_file, dir_file_new))
                count += 1
    print('%s files changed' % count)


if __name__ == '__main__':
    main()
