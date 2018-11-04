'''
Created on Oct 28, 2018

@author: krse
'''
import os
import sys


class DataProperties:
    def __init__(self, files):
        self.files = files
        self.adresar = "share:videa:matematika:blackpenredpen:calculus:02:"
        self.index = 0
        self.index_file = 1
        self.max_num = 0


def print_data(dp):
    sys.stdout.write("\n</datatables>")
    dp.max_num = len(dp.files)  # size of array

    for filename in dp.files:
        if dp.index == 0:
            ret_0 = "|{{" + dp.adresar + filename
        else:
            ret_0 = "{{" + dp.adresar + filename

        ret_1 = "}} \\\ (" + str(dp.index_file) + "/" + str(dp.max_num) + ") " + filename.replace("_", " ") \
                + "\\\ <fs smaller> poznamky...</fs>" + "|"

        sys.stdout.write(ret_0 + ret_1.replace(".mp4", ""))
        sys.stdout.flush()

        dp.index = dp.index + 1
        dp.index_file = dp.index_file + 1

        if dp.index > 3:
            sys.stdout.write("\n")
            dp.index = 0


def setup_data():

    for dirs, root, files in os.walk("/home/krse/Downloads/test"):
        # triedenie 1,2,3,4,5,6,7,8,9,10,11,12...    key=lambda f: int(filter(str.isdigit, f))

        dp = DataProperties(files)
        sys.stdout.write("<datatables ordering=\"false\">\n^video^video^video^video^\n")

        files.sort(key=lambda x: int(os.path.splitext(x)[0]))
        print_data(dp)
        sys.stdout.write("\n</datatables>")


def main():
    setup_data()


if __name__ == "__main__":
    main()


