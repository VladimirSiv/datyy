import dash_html_components as html
import dash_core_components as dcc


def network_graph(id_, title):
    """Generates network graph component

    Args:
        id_ (str): Component id
        title (str): Component text

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card title-centered",
        children=[
            html.Div(title, className="main-text-primary title-bold"),
            html.Hr(),
            dcc.Graph(id=id_),
        ],
    )
