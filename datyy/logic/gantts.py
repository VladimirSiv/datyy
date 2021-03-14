from datetime import datetime
import plotly.figure_factory as ff
import numpy as np
from styles.graphs import (
    GRAPH_BACKGROUND_COLOR,
    GANTT_GRAPH_COLORS,
    LINE_GRAPH_GRID_COLOR,
)

from faker import Faker

fake = Faker()


def simple_gantt_logic():
    """Generates gantt graph figure

    Returns:
        obj: Plotly figure

    """
    num = 9
    labels = fake.words(nb=5, unique=True)
    colors = {labels[i]: GANTT_GRAPH_COLORS[i] for i in range(len(labels))}
    data = [
        dict(
            Task=fake.word()[:6],
            Start=datetime(
                2020, np.random.randint(i + 1, 11), np.random.randint(1, 15)
            ).strftime("%Y-%m-%d"),
            Finish=datetime(
                2020, np.random.randint(i + 2, 11), np.random.randint(1, 15)
            ).strftime("%Y-%m-%d"),
            Resource=fake.random_choices(elements=labels, length=1)[0],
        )
        for i in range(num)
    ]

    fig = ff.create_gantt(
        data,
        colors=colors,
        index_col="Resource",
        show_colorbar=True,
        showgrid_x=True,
        showgrid_y=True,
    )
    fig.update_layout(
        paper_bgcolor=GRAPH_BACKGROUND_COLOR,
        plot_bgcolor=GRAPH_BACKGROUND_COLOR,
        title="",
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
    )
    return fig
