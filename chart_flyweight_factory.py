from chart_flyweight import ChartFlyweight
import pygal


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