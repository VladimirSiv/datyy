from datetime import date, timedelta
import numpy as np
import plotly.graph_objects as go
from styles.graphs import (
    GRAPH_BACKGROUND_COLOR,
    LINE_GRAPH_COLOR,
    LINE_GRAPH_GRID_COLOR,
    MULTILINE_GRAPH_COLORS,
    AREA_GRAPH_COLORS,
    ERROR_GRAPH_COLORS,
    AREA_GRAPH_FILL_COLOR,
)

from faker import Faker

fake = Faker()


def single_line_graph_logic():
    """Generates single line graph figure

    Returns:
        obj: Plotly figure

    """
    x_values = _get_dates()
    y_values = np.random.randint(60, size=len(x_values))
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x_values,
                y=y_values,
                mode="lines+markers",
                marker=dict(size=10),
                line=dict(
                    width=3,
                    color=MULTILINE_GRAPH_COLORS[int(np.random.randint(0, 5))],
                    dash="solid",
                ),
                name=fake.word(),
            ),
        ],
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
            yaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
            hovermode="x unified",
        ),
    )
    return fig


def multiline_graph_logic(num, dashed_lines=False, options=None, values=None):
    """Generates multiline graph figure

    Args:
        num (int): Number of lines
        dashed_lines (bool): Style lines. Defaults to False.
        options (list): List of item options
        values (list): List of item values

    Returns:
        obj: Plotly figure

    """
    text = fake.words(nb=num, unique=True)
    if options and values:
        text = [
            x["label"] for x in options if x["value"] in values
        ]  # no need to care about the order, dummy data
    colors = MULTILINE_GRAPH_COLORS[:num]
    lines_styles = ["solid"] * num
    if dashed_lines:
        lines_styles = ["solid", "dot", "dash", "longdash", "longdashdot"]
    x_values = _get_dates()
    y_values = [
        np.random.randint(np.random.randint(30, 60), size=len(x_values))
        for _ in range(num)
    ]
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x_values,
                y=yi,
                mode="lines+markers",
                marker=dict(size=10),
                line=dict(width=3, color=color, dash=dash_style),
                name=name,
            )
            for yi, name, color, dash_style in zip(y_values, text, colors, lines_styles)
        ],
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
            yaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
            hovermode="x unified",
        ),
    )
    return fig


def filled_graph_logic(num):
    """Generates filled graph figure

    Args:
        num (int): Number of filled lines

    Returns:
        obj: Plotly figure

    """
    x_values = _get_dates()
    y_values = [np.random.randint(0, 30, size=len(x_values)) for _ in range(num)]
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x_values,
                y=yi,
                fill="tozeroy",
                fillcolor=color_fill,
                line=dict(width=2, color=color),
                name=fake.word(),
            )
            for yi, color, color_fill in zip(
                y_values, AREA_GRAPH_COLORS, AREA_GRAPH_FILL_COLOR
            )
        ],
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
            yaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
        ),
    )
    return fig


def error_brands_graph_logic():
    """Generates error brand graph figures

    Returns:
        obj: Plotly figure

    """

    def generate_line_with_errors(num):
        """Generates plot data for error band figure

        Args:
            num (int): Number of lines with bar errors

        Returns:
            list: List of plotly Scatter objects

        """
        result = []
        for i in range(num):
            x_values = np.arange(60)
            y_values = np.random.randint(10, 60, size=60)
            e_values = np.random.uniform(4, 7, [60])
            result.extend(
                [
                    go.Scatter(
                        name=fake.word(),
                        x=x_values,
                        y=y_values,
                        mode="lines",
                        line=dict(width=3, color=ERROR_GRAPH_COLORS[i]),
                    ),
                    go.Scatter(
                        name=fake.word(),
                        x=x_values,
                        y=y_values + e_values,
                        mode="lines",
                        line=dict(width=0, color=ERROR_GRAPH_COLORS[i + 2]),
                        showlegend=False,
                    ),
                    go.Scatter(
                        name=fake.word(),
                        x=x_values,
                        y=y_values - e_values,
                        line=dict(width=0, color=ERROR_GRAPH_COLORS[i + 2]),
                        mode="lines",
                        fillcolor=ERROR_GRAPH_COLORS[i + 2],
                        fill="tonexty",
                        showlegend=False,
                    ),
                ]
            )
        return result

    fig = go.Figure(
        generate_line_with_errors(2),
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            xaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
            yaxis={
                "gridcolor": LINE_GRAPH_GRID_COLOR,
                "zerolinecolor": LINE_GRAPH_GRID_COLOR,
                "showspikes": True,
            },
        ),
    )
    return fig


def trend_graph_logic():
    """Generates trend graph figure

    Returns:
        obj: Plotly figure

    """
    x_values = np.arange(10)
    y_values = np.random.randint(10, size=10)
    fig = go.Figure(
        data=go.Scatter(
            x=x_values, y=y_values, fill="tozeroy", line=dict(color=LINE_GRAPH_COLOR)
        ),
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            height=100,
            showlegend=False,
            xaxis={"visible": False, "zeroline": False, "showgrid": False},
            yaxis={"visible": False, "zeroline": False},
        ),
    )
    return fig


def _get_dates():
    """Helper function for generating dates

    Returns:
        list: List of datetime objects

    """
    return [date.today() - timedelta(days=i) for i in range(15)]
