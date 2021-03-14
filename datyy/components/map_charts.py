import dash_html_components as html
import dash_core_components as dcc


def simple_map_graph(id_, title):
    """Generates simple map graph component

    Args:
        id_ (str): Component id
        title (str): Component text

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card mb-4",
        children=[
            html.Div(title, className="title-centered title-bold"),
            html.Hr(),
            dcc.Graph(id=id_),
        ],
    )
