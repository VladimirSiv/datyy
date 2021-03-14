import plotly.graph_objs as go
import numpy as np
from igraph import Graph
from faker import Faker
from styles.graphs import GRAPH_BACKGROUND_COLOR, NETWORK_MARKER_COLORS

fake = Faker()


def network_graph_logic():
    """Generates network graph figure

    Returns:
        obj: Plotly figure

    """
    graph = Graph.Erdos_Renyi(n=20, m=40)
    giant = graph.clusters().giant()
    giant["name"] = fake.words(nb=len(giant.vs), unique=True)
    group = [np.random.randint(1, 5) for _ in range(len(giant.vs))]
    size = [np.random.randint(6, 20) for _ in range(len(giant.vs))]
    vertices_coordinates, edges_coordinates = _get_edges_vertices_coordinates(giant)
    edges = go.Scatter3d(
        x=edges_coordinates[0],
        y=edges_coordinates[1],
        z=edges_coordinates[2],
        mode="lines",
        line=dict(color="rgb(125,125,125)", width=1),
        hoverinfo="none",
    )

    vertices = go.Scatter3d(
        x=vertices_coordinates[0],
        y=vertices_coordinates[1],
        z=vertices_coordinates[2],
        mode="markers",
        name="actors",
        marker=dict(
            symbol="circle",
            size=size,
            color=group,
            colorscale=NETWORK_MARKER_COLORS,
            line=dict(color="rgb(50,50,50)", width=0.5),
        ),
        text=giant["name"],
        hoverinfo="text",
    )

    axis = dict(
        showbackground=False,
        showline=False,
        zeroline=False,
        showgrid=False,
        showticklabels=False,
        title="",
    )

    layout = go.Layout(
        showlegend=False,
        paper_bgcolor=GRAPH_BACKGROUND_COLOR,
        plot_bgcolor=GRAPH_BACKGROUND_COLOR,
        scene=dict(
            xaxis=dict(axis),
            yaxis=dict(axis),
            zaxis=dict(axis),
        ),
        margin=dict(t=0, l=0, r=0, b=0),
        hovermode="closest",
    )
    return go.Figure(data=[vertices, edges], layout=layout)


def _get_edges_vertices_coordinates(graph):
    """Helper function for generating vertices and edges coordinates

    Args:
        graph (obj): Graph object

    Returns:
        list: List of vertices coordinates: x, y, z
        list: List of edges coordinates: x, y, z

    """
    layt = graph.layout("fr", dim=3)
    number_of_vertices = len(graph.vs)
    x_vertices = [layt[k][0] for k in range(number_of_vertices)]
    y_vertices = [layt[k][1] for k in range(number_of_vertices)]
    z_vertices = [layt[k][2] for k in range(number_of_vertices)]
    x_edges = []
    y_edges = []
    z_edges = []
    for edge in graph.es:
        x_edges += [layt[edge.source][0], layt[edge.target][0], None]
        y_edges += [layt[edge.source][1], layt[edge.target][1], None]
        z_edges += [layt[edge.source][2], layt[edge.target][2], None]
    vertices = [x_vertices, y_vertices, z_vertices]
    edges = [x_edges, y_edges, z_edges]
    return vertices, edges
