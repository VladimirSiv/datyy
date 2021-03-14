import dash_html_components as html
import dash_core_components as dcc
from components.radioitems import radio_items
from logic.defaults import default_figure


def line_graph_with_radio_items():
    """Generates line graph with radio items component

    Returns:
        obj: Html div object

    """
    graph = html.Div(
        className="main-card",
        children=[
            radio_items(id_="radioitems-input", num=3),
            dcc.Graph(id="summary-service-calls-graph"),
        ],
    )
    return graph


def line_graph_trend_section(id_, title):
    """Generates line graph trend section component

    Args:
        id_ (str): Component id
        title (str): Component text

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card title-centered trend-section",
        children=[
            html.Div(title, className="main-text-secondary"),
            html.Hr(),
            dcc.Graph(id=id_),
        ],
    )


def line_graph_with_title(id_, title, default_fig=False, default_fig_text=None):
    """Generates line graph with title component

    Args:
        id_ (str): Component id
        title (str): Component text
        default_fig (bool): Use default figure. Defaults to False
        default_fig_text (str): Default figure text. Defaults to None

    Returns:
        obj: Html div object

    """
    components = [
        html.Div(title, className="main-text-primary title-bold"),
        html.Hr(),
    ]
    if not default_fig:
        components.append(dcc.Graph(id=id_))
    else:
        components.append(dcc.Graph(id=id_, figure=default_figure(default_fig_text)))
    return html.Div(className="main-card title-centered", children=components)
