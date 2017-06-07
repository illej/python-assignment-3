from chart_flyweight_factory import ChartFlyweightFactory
# import pygal


class Visualiser(object):
    def __init__(self):
        self.__factory = ChartFlyweightFactory()

    def display_chart(self, arg, data):
        chart = self.__factory.get_flyweight(arg)
        chart.add_data(data)
        chart.make_title(data)
        chart.render()
