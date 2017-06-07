from file_builder import FileBuilder
from glob import glob


class TxtBuilder(FileBuilder):
    def __init__(self):
        super().__init__()

    def read(self):
        filename_list = glob('*.txt')
        print(filename_list)

        for file in filename_list:
            with open(file, 'r') as f:
                contents = f.read()
                self._raw_data.append(contents)

    def format(self):
        for file in self._raw_data:
            data_sets = file.split('\n\n')
            for data_set in data_sets:
                self._file.add(data_set)