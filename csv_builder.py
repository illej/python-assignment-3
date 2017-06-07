from file_builder import FileBuilder
from glob import glob
import csv


class CsvBuilder(FileBuilder):
    def __init__(self):
        super().__init__()

    def read(self):
        filename_list = glob('*.csv')
        print(filename_list)

        for file in filename_list:
            with open(file, 'r') as f:
                reader = csv.DictReader(f)
                data_list = list(reader)
                self._raw_data.append(data_list)

    def format(self):
        for data_sets in self._raw_data:
            for data_set in data_sets:
                str_set = ''
                for key, value in data_set.items():
                    str_row = key.lower() + '=' + value + '\n'
                    str_set += str_row
                self._file.add(str_set)
