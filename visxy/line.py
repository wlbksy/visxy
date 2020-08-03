from typing import Optional

from .cartesian import Cartesian


class Line(Cartesian):
    def __init__(self):
        self.figure_type = "line"

        super().__init__()
        super().set_figure_type(self.figure_type)
        super().set_page_title(self.figure_type)

    def set_series_visual(
        self,
        symbol: Optional[str] = "emptyCircle",
        symbol_size: int = 4,
        line_color: Optional[str] = None,
        line_width: int = 2,
        line_type: str = "solid",
        line_opacity: float = 1,
    ):
        for series in self.series[-self.last_series_len :]:
            if symbol_size != 4:
                series["symbolSize"] = symbol_size
            if symbol in [
                "circle",
                "rect",
                "roundRect",
                "triangle",
                "diamond",
                "pin",
                "arrow",
                "none",
            ]:
                series["symbol"] = symbol
            if symbol is None:
                series["showSymbol"] = 0

            if line_color is not None:
                if "lineStyle" not in series:
                    series["lineStyle"] = {}
                series["lineStyle"]["color"] = line_color
            if line_width != 2:
                if "lineStyle" not in series:
                    series["lineStyle"] = {}
                series["lineStyle"]["width"] = line_width
            if line_type in ["dashed", "dotted"]:
                if "lineStyle" not in series:
                    series["lineStyle"] = {}
                series["lineStyle"]["type"] = line_type
            if 0.0 <= line_opacity < 1.0:
                if "lineStyle" not in series:
                    series["lineStyle"] = {}
                series["lineStyle"]["opacity"] = line_opacity
