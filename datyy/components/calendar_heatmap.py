import dash_html_components as html
import dash_core_components as dcc


def calendar_heatmap(id_, title):
    """Generates calendar heatmap chart component

    Args:
        id_ (str): Component id
        title (str): Component title

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card",
        children=[
            html.Div(
                title,
                className="title-bold title-centered",
            ),
            html.Hr(),
            dcc.Graph(id=id_),
        ],
    )
