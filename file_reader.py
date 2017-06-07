import os
from file_read_director import FileReadDirector
from txt_builder import TxtBuilder
from csv_builder import CsvBuilder


class FileReader(object):
    def __init__(self):
        self.__all_sets = []
        self.__products = []
        self.__director = FileReadDirector()
        self.__builders = [TxtBuilder(),
                           CsvBuilder()]

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
            for builder in self.__builders:
                self.__director.set_builder(builder)
                self.__director.construct()
                self.__products.append(builder.get_file())

            for product in self.__products:
                self._add_to_all(product.get_contents())

            return self.__all_sets

    def _add_to_all(self, contents):
        for data_set in contents:
            self.__all_sets.append(data_set)


if __name__ == '__main__':  # pragma: no cover
    import doctest

    doctest.testmod()
