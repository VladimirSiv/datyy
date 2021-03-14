import dash_html_components as html
import dash_core_components as dcc


def select_date(id_, date_min, date_max, text=None):
    """Generates select date component

    Args:
        id_ (str): Component id
        date_min (datetime): Minimum select date
        date_max (datetime): Maximum select date
        text (str, optional): Component text next to picker

    Returns:
        obj: Html div object

    """
    components = []
    if text:
        components.append(html.Div(text, className="select-date-text"))
    components.append(
        dcc.DatePickerSingle(id=id_, min_date_allowed=date_min, max_date_allowed=date_max)
    )
    return html.Div(className="main-row select-date mb-4", children=components)
