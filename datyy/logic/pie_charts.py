import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from styles.graphs import (
    GRAPH_BACKGROUND_COLOR,
    PIE_GRAPH_COLORS_DIVERGENT,
    PIE_GRAPH_COLORS_MASTER,
    SUNBURST_GRAPH_COLORS,
)
from faker import Faker

fake = Faker()


def simple_pie_chart_logic():
    """Generates simple pie chart figure

    Returns:
        obj: Plotly figure

    """
    labels = fake.words(nb=5, unique=True)
    values = [4500, 2500, 1500, 1053, 500]
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                textinfo="label",
                insidetextorientation="radial",
                marker_colors=PIE_GRAPH_COLORS_MASTER,
            )
        ],
        layout=go.Layout(
            showlegend=False,
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
        ),
    )
    return fig


def simple_ring_chart_logic():
    """Generates simple ring chart figure

    Returns:
        obj: Plotly figure

    """
    labels = [*["Prod. " + fake.word()[:3] for _ in range(5)], "Other"]
    values = [4500, 2500, 1053, 1500, 500, 400]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                textinfo="label",
                insidetextorientation="radial",
                hole=0.3,
                marker_colors=PIE_GRAPH_COLORS_DIVERGENT,
            )
        ],
        layout=go.Layout(
            showlegend=False,
            paper_bgcolor=GRAPH_BACKGROUND_COLOR,
            plot_bgcolor=GRAPH_BACKGROUND_COLOR,
            height=350,
            margin=dict(t=20, b=20, l=20, r=20),
        ),
    )
    return fig


def sunburst_chart_logic():
    """Generates sunburst chart figure

    Returns:
        obj: Plotly figure

    """
    num = 10
    variables = ["flu", "satellite", "plead"]
    x_values = fake.words(nb=num, unique=True)
    y_values = [fake.random_choices(elements=variables, length=1)[0] for _ in range(num)]
    z_values = [*["reactor"] * 5, *["great"] * 5]
    k_values = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
    data = pd.DataFrame(dict(x=x_values, y=y_values, z=z_values, k=k_values))
    fig = px.sunburst(
        data,
        path=["z", "y", "x"],
        values="k",
        color="y",
        color_discrete_map={
            "(?)": SUNBURST_GRAPH_COLORS[0],
            "flu": SUNBURST_GRAPH_COLORS[1],
            "satellite": SUNBURST_GRAPH_COLORS[2],
            "plead": SUNBURST_GRAPH_COLORS[3],
        },
    )
    fig.update_layout(
        showlegend=False,
        paper_bgcolor=GRAPH_BACKGROUND_COLOR,
        plot_bgcolor=GRAPH_BACKGROUND_COLOR,
        height=350,
        margin=dict(t=20, b=20, l=20, r=20),
    )
    return fig
