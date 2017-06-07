import pygal


class Visualiser(object):
    def __init__(self):
        self.__charts = {'-b': pygal.Bar(),
                         '-l': pygal.Line(),
                         '-p': pygal.Pie(),
                         '-r': pygal.Radar()}
        self.test_fw()

    def display_chart(self, arg, data):
        obj = self.__charts[arg]
        chart = self.build_chart(obj, data)
        chart.render_in_browser()

    def build_chart(self, obj, data):
        chart = obj
        title_builder = []
        for key, data_list in data.items():
            title_builder.append(key + ' vs ')
            chart.add(key, data_list)
            chart.title = ''.join(title_builder)[:-4]
        return chart

    def is_valid_flag(self, input_param):
        result = False
        if input_param in self.__charts:
            result = True
        return result

    def test_fw(self):
        factory = ChartFlyweightFactory()
        chart = factory.get_flyweight('-b')
        chart.say()


class ChartFlyweightFactory(object):
    def __init__(self):
        self.pool = {}

    def get_flyweight(self, key):
        if key not in self.pool:
            self.pool[key] = self.make_flyweight(key)
        return self.pool[key]

    def make_flyweight(self, key):
        charts = {'-b': pygal.Bar,
                  '-l': pygal.Line,
                  '-p': pygal.Pie,
                  '-r': pygal.Radar}
        return ChartFlyweight(charts[key])


class ChartFlyweight(object):
    def __init__(self, chart):
        self.object = chart()

    def say(self):
        print(self.object)
