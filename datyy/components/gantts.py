import dash_core_components as dcc
import dash_html_components as html


def simple_gantt_graph(id_):
    """Generates simple gantt chart component

    Args:
        id_ (str): Component id

    Returns:
        obj: Html div object

    """
    return html.Div(className="main-card", children=[dcc.Graph(id=id_)])
