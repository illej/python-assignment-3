from abc import ABCMeta, abstractmethod
from data_file import DataFile


class FileBuilder(metaclass=ABCMeta):
    def __init__(self):
        self._file = None
        self._raw_data = []

    def create_file(self):
        self._file = DataFile()

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def format(self):
        raise NotImplementedError

    def get_file(self):
        return self._file
