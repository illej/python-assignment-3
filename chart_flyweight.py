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
