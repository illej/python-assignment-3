import os
import csv
from glob import glob
from abc import ABCMeta, abstractmethod
from file_read_director import FileReadDirector
from txt_builder import TxtBuilder
from csv_builder import CsvBuilder


class FileReader(object):

    def read_file(self, line):
        """
        >>> file_list = FileReader().read_file('')
        ['data.txt', 'data2.txt', 'data3.txt', 'datalist.txt', 'file.txt']
        >>> file_list[0]
        'empid=D011\\ngender=m\\nage=29\\nsales=722\\nbmi=normal\\nsalary=320\\nbirthday=23-11-1987'
        """
        if line:
            flag = line.split()
            if flag[0] == 'cwd':
                print(os.getcwd())
                contents = os.listdir(os.getcwd())
                for item in contents:
                    if item[-4:] != '.txt' and item[-3:] != '.py' and item[-3:] != '.db':
                        print(item)
            elif len(flag) == 1:
                try:
                    directory = './' + line
                    os.chdir(directory)
                    print(os.getcwd())
                except Exception as e:
                    print('fview:', e)
        else:
            # raw_file_list = []
            # filename_list = glob('*.txt')
            # print(filename_list)
            # for file in filename_list:
            #     with open(file, 'r') as f:
            #         contents = f.read()
            #         data_sets = contents.split("\n\n")
            #         for data_set in data_sets:
            #             raw_file_list.append(data_set)

            all_sets = []

            txt_builder = TxtBuilder()
            director = FileReadDirector(txt_builder)
            director.construct()
            txt_file = txt_builder.get_file()
            txt_contents = txt_file.get_contents()

            for data_set in txt_contents:
                all_sets.append(data_set)

            csv_builder = CsvBuilder()
            director.set_builder(csv_builder)
            director.construct()
            csv_file = csv_builder.get_file()
            csv_contents = csv_file.get_contents()

            for data_set in csv_contents:
                all_sets.append(data_set)

            return all_sets


if __name__ == '__main__':  # pragma: no cover
    import doctest

    doctest.testmod()
