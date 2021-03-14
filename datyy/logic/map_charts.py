import plotly.graph_objects as go
import numpy as np
from styles.graphs import GRAPH_BACKGROUND_COLOR, MAP_MARKER_COLORS
from faker import Faker

fake = Faker()


def simple_map_graph_logic():
    """Generates simple map graph figure

    Returns:
        obj: Plotly figure

    """
    limits = [(0, 2), (3, 10), (11, 20), (21, 50), (50, 3000)]
    scale = 5000
    fig = go.Figure()
    for i, lim in enumerate(limits):
        place = [fake.local_latlng() for _ in range(20)]
        lat = [x[0] for x in place]
        lon = [x[1] for x in place]
        text = [x[2] for x in place]
        pop = np.random.randint(100000, 1000000, size=20)
        fig.add_trace(
            go.Scattergeo(
                locationmode="USA-states",
                lon=lon,
                lat=lat,
                text=text,
                marker=dict(
                    size=pop / scale,
                    color=MAP_MARKER_COLORS[i],
                    line_color="rgb(40,40,40)",
                    line_width=0.5,
                    sizemode="area",
                ),
                name="{0} - {1}".format(lim[0], lim[1]),
            )
        )
    fig.update_layout(
        showlegend=True,
        geo=dict(
            scope="usa", landcolor="rgb(217, 217, 217)", bgcolor=GRAPH_BACKGROUND_COLOR
        ),
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor=GRAPH_BACKGROUND_COLOR,
        plot_bgcolor=GRAPH_BACKGROUND_COLOR,
    )
    return fig
