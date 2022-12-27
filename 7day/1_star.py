import string
import re


class Folder:

    def __init__(self, name, dpath=[], files=[]):
        self.name: str = name
        self.dpath: list = dpath
        self._files: list = files
        self.depth: int = len(dpath)
        self.linux_path: str = self.create_lpath()

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value.copy()

    def add_file(self, value):
        self._files.append(value)

    def get_disk_usage(self):
        return sum(self.files)

    def create_lpath(self):
        if self.name != '/':
            return '/'.join(self.dpath)[1:]
        else:
            return '/'


def load_input():
    with open('inputs.txt', mode='r') as file:
        content = file.readlines()
        return content


def transform_input(input: str):
    folders = []
    dpath = []
    files = []
    folder = None
    current_folder = ''
    depth = 1
    for command in input:
        command = command.strip()

        if '$ cd' in command and command != '$ cd ..':
            current_folder = command[5:]
            dpath.append(current_folder)
            if depth != len(dpath):
                folder.files = files
                files.clear()
                folders.append(folder)
            folder = Folder(current_folder, dpath.copy())
            depth = len(dpath)

        handle_content(command, files)

        if command == '$ cd ..':    
            current_folder = dpath.pop()
            depth = len(dpath)

    folder.files = files
    folders.append(folder)
    return folders


def handle_content(command, files: list):
    pattern = '[0-9]+'
    if command[1] in string.digits:
        result = re.search(pattern, command)
        files.append(int(result.group()))


def get_parent(folders: list[Folder], linux_path):
    if len(linux_path) > 2:
        linux_path = linux_path[:-1]
    for folder in folders:
        if folder.linux_path == linux_path:
            return folder


def main():
    terminal_log = load_input()
    folders = transform_input(terminal_log)
    folders.sort(key=lambda x: x.depth, reverse=True)

    for folder in folders:
        print(folder.__dict__)
        files_usg = folder.get_disk_usage()
        parent = get_parent(
            folders, folder.linux_path[:-len(folder.name)])
        if parent:
            parent.add_file(files_usg)

    result = 0

    for folder in folders:
        files_usg = folder.get_disk_usage()
        if 100000 > files_usg:
            result += files_usg

    print(result)


if __name__ == '__main__':
    main()
