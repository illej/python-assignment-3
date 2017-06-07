class Controller(object):
    def __init__(self, cmdview, file_reader, parser, validator, db, vis, serial):
        self.__cmdview = cmdview
        self.__file_reader = file_reader
        self.__parser = parser
        self.__validator = validator
        self.__db = db
        self.__vis = vis
        self.__serial = serial

    def display(self, line=None):
        try:
            if line:
                data_set_dict = {}
                input_params = line.split()
                # print("input: ", input)
                if len(input_params) > 1:
                    if self.__validator.is_valid_column(input_params[1]):
                        iterinput = iter(input_params)
                        next(iterinput)
                        for data_set in iterinput:
                            data = self.__db.retrieve(data_set)
                            clean_data = self.__parser.scrub_db_list(data)
                            data_set_dict[data_set] = clean_data
                        self.__vis.display_chart(input_params[0], data_set_dict)
                    else:
                        raise Exception("-- Invalid data.")
                else:
                    raise Exception(
                        "* Invalid input. \n-- Type 'help display' for information on how to use this command.")
            else:
                raise Exception(
                    "* Missing parameters. \n-- Type 'help display' for information on how to use this command.")
        except Exception as e:
            print(e)

    def validate(self):
        try:
            if self.__parser.get_data():
                data_sets = self.__parser.get_data()
                for data_set in data_sets:
                    self.__validator.validate(data_set)
            else:
                raise Exception("* No data has been read.\n-- Type 'help get' for more details.")
        except Exception as e:
            print(e)

    def commit(self):
        try:
            valid_data = self.__validator.get_valid_sets()
            for data_set in valid_data:
                self.__db.insert(data_set)
        except Exception as e:
            print(e)
            print("* Could not commit data to the database.\n-- Type 'help commit' for more details.")

    def rebuild_db(self):
        self.__db.rebuild()

    # NEW FILE READING METHOD
    def get(self, line):
        try:
            data_sets = self.__file_reader.read_file(line)
            for index, data_set in enumerate(data_sets):  # TODO: don't need enumeration?
                self.__parser.parse_raw_data(data_set)
        except Exception as e:
            pass

    def query(self, line):
        print(self.__db.retrieve(line))
        # clean = self.__parser.scrub_db_list(self.__db.retrieve(line))
        # print(clean)

    def serialize(self, line):
        db_contents = self.__db.retrieve('*')
        self.__serial.serialize(line, db_contents)
