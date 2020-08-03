from .cartesian import Cartesian


class Scatter(Cartesian):
    def __init__(self):
        self.figure_type = "scatter"

        super().__init__()
        super().set_figure_type(self.figure_type)
        super().set_page_title(self.figure_type)

    def set_series_visual(self, symbol: str = "circle", symbol_size: int = 10):
        for series in self.series[-self.last_series_len :]:
            if symbol in [
                "rect",
                "roundRect",
                "triangle",
                "diamond",
                "pin",
                "arrow",
                "none",
            ]:
                series["symbol"] = symbol
            if symbol_size != 10:
                series["symbolSize"] = symbol_size
