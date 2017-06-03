from glob import glob
import os


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

            builder = TxtBuilder()
            director = FileReadDirector(builder)
            director.construct()
            file = builder.get_file()
            contents = file.get_contents()

            return contents

        class FileReadDirector(object):
            def __init__(self, file_builder):
                self.__fileBuilder = file_builder

            def set_builder(self, file_builder):
                self.__fileBuilder = file_builder

            def construct(self):
                self.__fileBuilder.create_file()
                self.__fileBuilder.read()
                self.__fileBuilder.format()

        class File(object):
            def __init__(self):
                self.__contents = []

            def set_contents(self, data):
                self.__contents.append(data)

            def get_contents(self):
                return self.__contents

        class Builder(metaclass=ABCMeta):
            def __init__(self):
                self._file = None
                # self._all_data_sets = []

            def create_file(self):
                self._file = File()

            @abstractmethod
            def read(self):
                raise NotImplementedError

            @abstractmethod
            def format(self):
                raise NotImplementedError

            def get_file(self):
                # return self._all_data_sets
                return self._file

        class TxtBuilder(Builder):
            def __init__(self):
                super().__init__()
                self.__raw_files = []

            def read(self):
                filename_list = glob('*.txt')
                print(filename_list)

                for file in filename_list:
                    with open(file, 'r') as f:
                        contents = f.read()
                        self.__raw_files.append(contents)

            def format(self):
                for file in self.__raw_files:
                    data_sets = file.split('\n\n')
                    for data_set in data_sets:
                        # self._all_data_sets.append(data_set)
                        self._file.set_contents(data_set)

if __name__ == '__main__':  # pragma: no cover
    import doctest

    doctest.testmod()
