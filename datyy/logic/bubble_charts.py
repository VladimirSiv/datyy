import numpy as np
import plotly.graph_objs as go
from styles.graphs import (
    GRAPH_BACKGROUND_COLOR,
    LINE_GRAPH_GRID_COLOR,
    BUBBLE_MARKER_COLORS,
)
from faker import Faker

fake = Faker()


def simple_bubble_chart_logic():
    """Generates bubble chart figure

    Returns:
        obj: Plotly figure

    """
    categories = fake.words(nb=5, unique=True)
    fig = go.Figure()
    for i, category in enumerate(categories):
        fig.add_trace(
            go.Scatter(
                x=np.random.uniform(0, 40, [10]),
                y=np.random.uniform(10, 100, [10]),
                marker_size=np.random.randint(20, 50, size=10),
                name=category,
                marker=dict(color=BUBBLE_MARKER_COLORS[i]),
            )
        )
    fig.update_traces(mode="markers")
    fig.update_layout(
        xaxis=dict(
            title="Amount ordered",
            gridcolor=LINE_GRAPH_GRID_COLOR,
            zerolinecolor=LINE_GRAPH_GRID_COLOR,
            gridwidth=2,
        ),
        yaxis=dict(
            title="Product Views",
            gridcolor=LINE_GRAPH_GRID_COLOR,
            zerolinecolor=LINE_GRAPH_GRID_COLOR,
            gridwidth=2,
        ),
        legend_title="Category",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor=GRAPH_BACKGROUND_COLOR,
        plot_bgcolor=GRAPH_BACKGROUND_COLOR,
    )
    return fig
