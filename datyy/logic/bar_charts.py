import plotly.graph_objects as go
import numpy as np
from styles.graphs import (
    GRAPH_BACKGROUND_COLOR,
    summary_bar_graph_colors,
    LINE_GRAPH_GRID_COLOR,
)
from faker import Faker

fake = Faker()


def simple_bar_chart_logic():
    """Generates simple bar chart figure

    Returns:
        obj: Plotly figure

    """
    x_values = fake.words(nb=10, unique=True)
    y_values = sorted(np.random.randint(100000, size=10), reverse=True)
    y2_values = sorted(np.random.randint(80000, size=10), reverse=True)
    fig = go.Figure(
        [
            go.Bar(
                x=x_values,
                y=y_values,
                text=y_values,
                name=fake.word(),
                cliponaxis=False,
                marker_color=summary_bar_graph_colors[0],
            ),
            go.Bar(
                x=x_values,
                y=y2_values,
                text=y2_values,
                name=fake.word(),
                cliponaxis=False,
                marker_color=summary_bar_graph_colors[1],
            ),
        ],
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
            yaxis={"visible": False, "zeroline": False},
            barmode="group",
            legend=dict(
                x=0.80,
                y=1.0,
                bgcolor="rgba(255, 255, 255, 0)",
                bordercolor="rgba(255, 255, 255, 0)",
            ),
        ),
    )
    fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
    return fig


def horizontal_bar_chart_logic():
    """Generates horizontal bar chart figure

    Returns:
        obj: Plotly figure

    """
    y_values = sorted([np.random.uniform(90, 95), *np.random.uniform(1, 50, [7])])
    x_values = fake.words(nb=8, unique=True)
    fig = go.Figure(
        [
            go.Bar(
                x=y_values,
                y=x_values,
                marker=dict(
                    color=y_values,
                    colorscale="Blugrn",
                    line=dict(color="rgba(50, 171, 96, 1.0)", width=1),
                ),
                orientation="h",
            ),
        ],
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=True,
                ticks="outside",
                ticklen=10,
            ),
            xaxis=dict(
                zeroline=False,
                showline=False,
                showticklabels=True,
                showgrid=True,
                gridcolor=LINE_GRAPH_GRID_COLOR,
                zerolinecolor=LINE_GRAPH_GRID_COLOR,
            ),
            barmode="group",
        ),
    )
    y_s = np.round(y_values, decimals=2)
    annotations = []
    for y_d, x_d in zip(y_s, x_values):
        annotations.append(
            dict(
                xref="x1",
                yref="y1",
                y=x_d,
                x=y_d + 5,
                text=str(y_d) + "%",
                font=dict(family="Arial", size=12, color="rgb(50, 171, 96)"),
                showarrow=False,
            )
        )
    fig.update_layout(annotations=annotations)
    return fig


def multi_group_bar_chart(num, options=None, values=None):
    """Generates multi group bar chart figure

    Returns:
        obj: Plotly figure

    """
    x_values = fake.words(nb=10, unique=True)
    text = fake.words(nb=num, unique=True)
    if options and values:
        text = [
            x["label"] for x in options if x["value"] in values
        ]  # no need to care about the order, dummy data
    y_values = [
        sorted(np.random.randint(100000, size=10), reverse=True) for _ in range(num)
    ]
    fig = go.Figure(
        [
            go.Bar(
                x=x_values,
                y=yi,
                text=yi,
                name=name,
                cliponaxis=False,
                marker_color=color,
            )
            for yi, name, color in zip(y_values, text, summary_bar_graph_colors[:num])
        ],
        layout=go.Layout(
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            margin=dict(t=20, b=20, l=20, r=20),
            yaxis={"visible": False, "zeroline": False},
            barmode="group",
            legend=dict(
                x=0.80,
                y=1.0,
                bgcolor="rgba(255, 255, 255, 0)",
                bordercolor="rgba(255, 255, 255, 0)",
            ),
        ),
    )
    return fig
