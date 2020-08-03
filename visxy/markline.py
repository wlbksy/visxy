from typing import Optional


def add_markline_parallel_to_axis(series, direction: str, values, tag: str):
    if "markLine" not in series:
        series["markLine"] = {}

    if "data" not in series["markLine"]:
        series["markLine"]["data"] = []

    _set_markline_symbol(series, start_symbol="none", end_symbol="none")

    if not isinstance(values, list):
        values = [values]

    for v in values:
        series["markLine"]["data"].append({direction: v})
    _set_markline_tag(series, tag)


def set_markline_visual_helper(
    series,
    tag: Optional[str] = None,
    line_color: Optional[str] = None,
    line_type: str = "dashed",
    start_symbol: str = "none",
    end_symbol: str = "none",
):
    assert "markLine" in series, "set markline visual after mark line data"
    _set_markline_symbol(series, start_symbol, end_symbol)
    _set_markline_type(series, line_type)
    _set_markline_tag(series, tag)
    # _set_markline_color(series, line_color)


def _set_markline_symbol(series, start_symbol: str, end_symbol: str):
    if start_symbol == "circle" and end_symbol == "arrow":
        return

    if "symbol" not in series["markLine"]:
        series["markLine"]["symbol"] = ["none", "none"]

    if start_symbol in ["rect", "roundRect", "triangle", "diamond", "pin", "arrow"]:
        series["symbol"][0] = start_symbol
    if end_symbol in ["circle", "rect", "roundRect", "triangle", "diamond", "pin"]:
        series["symbol"][1] = end_symbol


def _set_markline_tag(series, tag: Optional[str] = None):
    if tag is None:
        return

    if "label" not in series["markLine"]:
        series["markLine"]["label"] = {"formatter": tag}

    series["markLine"]["tooltip"] = {}


def _set_markline_type(series, line_type: str):
    if line_type not in ["solid", "dotted"]:
        return

    if "lineStyle" not in series["markLine"]:
        series["markLine"]["lineStyle"] = {}

    series["markLine"]["lineStyle"]["type"] = line_type


def _set_markline_color(series, line_color: Optional[str] = None):
    if line_color is None:
        return

    if "lineStyle" not in series["markLine"]:
        series["markLine"]["lineStyle"] = {}

    series["markLine"]["lineStyle"]["color"] = line_color
