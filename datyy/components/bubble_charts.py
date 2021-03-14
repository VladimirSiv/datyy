import dash_html_components as html
import dash_core_components as dcc


def simple_bubble_chart(id_, title):
    """Generates simple bubble chart component

    Args:
        id (str): Component id
        title (str): Component title

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card mb-4",
        children=[
            html.Div(
                title,
                className="title-bold title-centered",
            ),
            html.Hr(),
            dcc.Graph(id=id_),
        ],
    )
