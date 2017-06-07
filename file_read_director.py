class FileReadDirector(object):
    def __init__(self):
        self.__file_builder = None

    def set_builder(self, file_builder):
        self.__file_builder = file_builder

    def construct(self):
        self.__file_builder.create_file()
        self.__file_builder.read()
        self.__file_builder.format()
