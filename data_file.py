class DataFile(object):
    def __init__(self):
        self.__contents = []

    def add(self, data):
        self.__contents.append(data)

    def get_contents(self):
        return self.__contents
