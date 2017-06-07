import pygal


class Visualiser(object):
    def __init__(self):
        # self.__charts = {'-b': pygal.Bar(),
        #                  '-l': pygal.Line(),
        #                  '-p': pygal.Pie(),
        #                  '-r': pygal.Radar()}
        self.factory = ChartFlyweightFactory()
        # self.test_fw()

    def display_chart(self, arg, data):
        # obj = self.__charts[arg]
        # chart = self.build_chart(obj, data)
        # chart.render_in_browser()

        chart = self.factory.get_flyweight(arg)
        chart.add_data(data)
        chart.make_title(data)
        chart.render()

    # def build_chart(self, obj, data):
    #     chart = obj
    #     title_builder = []
    #     for key, data_list in data.items():
    #         title_builder.append(key + ' vs ')
    #         chart.add(key, data_list)
    #         chart.title = ''.join(title_builder)[:-4]
    #     return chart
    #
    # def is_valid_flag(self, input_param):
    #     result = False
    #     if input_param in self.__charts:
    #         result = True
    #     return result


class ChartFlyweightFactory(object):
    def __init__(self):
        self.__pool = {}
        self.__charts = {'-b': pygal.Bar,
                         '-l': pygal.Line,
                         '-p': pygal.Pie,
                         '-r': pygal.Radar}

    def get_flyweight(self, key):
        if key not in self.__pool:
            self.__pool[key] = self.make_flyweight(key)
        return self.__pool[key]

    def make_flyweight(self, key):
        assert key in self.__charts, "-- Invalid flag."
        return ChartFlyweight(self.__charts[key])


class ChartFlyweight(object):
    def __init__(self, chart):
        self.__chart = chart()

    def add_data(self, data):
        for key, data_list in data.items():
            self.__chart.add(key, data_list)

    def make_title(self, data):
        parts = []
        for key in data:
            parts.append(key + ' vs ')
        self.__chart.title = ''.join(parts)[:-4]

    def render(self):
        self.__chart.render_in_browser()
