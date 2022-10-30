import sys
import os
import re


class Compare:

    def __init__(self, path1, path2):
        self.path1_set = self.path_to_set(path1)
        self.path2_set = self.path_to_set(path2)

    def path_to_set(self, path):
        s = set()
        for elem in os.listdir(path):
            s.add(self.process(elem))

        return s

    def only_1(self):
        return self.path1_set - self.path2_set

    def only_2(self):
        return self.path2_set - self.path1_set

    # Removes .icloud file extension
    def process(self, filename):
        pattern = re.compile("\.?(.*)\.icloud")
        result = pattern.match(filename)

        if result:
            return result.group(1)
        else:
            return filename


if __name__ == "__main__":
    c = Compare(sys.argv[1], sys.argv[2])

    # will print the needed commands
    command1 = "cd " + sys.argv[1].replace(" ", "\ ") + " && " "cp "
    command2 = "cd " + sys.argv[2].replace(" ", "\ ") + " && " "cp "

    print("Only in (1) " + sys.argv[1])
    for file in c.only_1():
        command1 += file.replace(" ", "\ ") + " "
        print("   - " + file)
    command1 += sys.argv[2].replace(" ", "\ ")

    print(command1)

    print("Only in (2) " + sys.argv[2])
    for file in c.only_2():
        command2 += file.replace(" ", "\ ") + " "
        print("   - " + file)
    command2 += sys.argv[1].replace(" ", "\ ") + " "

    print(command2)
