import dash_core_components as dcc
import dash_html_components as html


def simple_pie_chart(id_, title=None):
    """Generates simple pie chart component

    Args:
        id_ (str): Component id
        title (str, optional): Component text. Defaults to None

    Returns:
        obj: Html div object

    """
    components = []
    if title:
        components.extend(
            [
                html.Div(
                    className="title-bold title-centered",
                    children=[title],
                ),
                html.Hr(),
            ]
        )
    components.append(dcc.Graph(id=id_))
    return html.Div(className="main-card", children=components)
