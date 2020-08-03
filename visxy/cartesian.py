import json
from typing import List, Optional, Union

from .markline import add_markline_parallel_to_axis, set_markline_visual_helper
from .tpl import get_template


class Cartesian:
    def __init__(self):
        self.theme = ""
        self.page_title = ""
        self.figure_title = ""
        self.dataset = []
        self.series = []
        self.x_axis_is_time = ""

        self.x_axis_name = ""
        self.y_axis_name = ""
        self.y_min = ""
        self.y_max = ""

        self.current_dataset_index = 0
        self.series_idx = 0
        self.last_series_len = 0

    def set_figure_type(self, figure_type: str):
        self.figure_type = figure_type

    def set_page_title(self, page_title: str):
        if page_title:
            self.page_title = page_title

    def set_figure_title(self, figure_title: str):
        if figure_title:
            self.figure_title = figure_title

    def set_theme(self, theme: str):
        if theme in ["light", "dark"]:
            self.theme = f", '{theme}'"

    def set_x_axis_as_time(self, flag: bool):
        if flag:
            self.x_axis_is_time = ", type: 'time'"

    def set_x_axis_name(self, x_axis_name: Optional[str] = None):
        if x_axis_name is not None and x_axis_name:
            self.x_axis_name = f', name: "{x_axis_name}"'

    def set_y_axis_name(self, y_axis_name: Optional[str] = None):
        if y_axis_name is not None and y_axis_name:
            self.y_axis_name = f'name: "{y_axis_name}"'

    def add_series(
        self,
        x_column: List[Union[int, float]],
        y_columns: Union[List[Union[int, float]], List[List[Union[int, float]]]],
        legends: Union[str, List[str]],
    ):
        if not isinstance(y_columns[0], list):
            y_columns = [y_columns]
            legends = [legends]

        dataset = {"source": [["x"] + x_column]}
        series_list = []
        for legend, column in zip(legends, y_columns):
            dataset["source"].append([legend] + column)
            series = {
                "name": legend,
                "type": self.figure_type,
                "encode": {"y": legend},
                "seriesLayoutBy": "row",
                "datasetIndex": self.current_dataset_index,
            }
            if self.figure_type == "scatter":
                series["large"] = 1
            series_list.append(series)

        self.current_dataset_index += 1
        self.last_series_len = len(series_list)

        self.dataset.append(dataset)
        self.series.extend(series_list)

    def add_markline_horizontal(self, y_list: List[float], tag: Optional[str]):
        self._add_empty_series(tag)
        add_markline_parallel_to_axis(
            series=self.series[-1], direction="yAxis", values=y_list, tag=tag
        )

    def add_markline_vertical(
        self, x_list: Union[float, List[float]], tag: Optional[str]
    ):
        self._add_empty_series(tag)
        add_markline_parallel_to_axis(
            series=self.series[-1], direction="xAxis", values=x_list, tag=tag
        )

    def set_markline_visual(
        self,
        tag: Optional[str] = None,
        line_color: Optional[str] = None,
        line_type: str = "dashed",
        start_symbol: str = "none",
        end_symbol: str = "none",
    ):
        set_markline_visual_helper(
            series=self.series[-1],
            tag=tag,
            line_color=line_color,
            line_type=line_type,
            start_symbol=start_symbol,
            end_symbol=end_symbol,
        )

    def render(self, fn=None):
        d = {
            "page_title": self.page_title,
            "theme": self.theme,
            "figure_title": self.figure_title,
            "xaxis_is_time": self.x_axis_is_time,
            "dataset": json.dumps(self.dataset, ensure_ascii=False),
            "series": json.dumps(self.series, ensure_ascii=False),
            "x_axis_name": self.x_axis_name,
            "y_axis_name": self.y_axis_name,
            "y_min": self.y_min,
            "y_max": self.y_max,
        }

        render_fn = fn
        if render_fn is None:
            render_fn = f"{self.page_title}.html"

        tpl = get_template()
        with open(render_fn, "w") as f:
            f.write(tpl.substitute(d))
        print(f"`{render_fn}` is rendered.")

    def _add_empty_series(self, tag):
        legends = "markline"
        if tag is not None:
            legends = tag
        self.add_series(x_column=[], y_columns=[[]], legends=[legends])
