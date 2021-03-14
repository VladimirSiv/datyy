import dash_core_components as dcc
import dash_html_components as html


def dropdown_single(id_, placeholder, text=None):
    """Generates single dropdown component

    Args:
        id_ (str): Component id
        placeholder (str): Component placeholder
        text (str, optional): Component text. Defaults to None

    Returns:
        obj: Html div object

    """
    components = []
    if text:
        components.append(html.Div(text, className="select-dropdown-text"))
    components.append(
        dcc.Dropdown(id=id_, placeholder=placeholder, style={"width": "200px"})
    )
    return html.Div(className="select-dropdown", children=components)


def dropdown_multiple(id_, placeholder, size="200px", text=None):
    """Generates multiple dropdown component

    Args:
        id_ (str): Component id
        placeholder (str): Component placeholder
        size (str, optional): Component size. Defaults to None
        text (str, optional): Component text. Defaults to None

    Returns:
        obj: Html div object

    """
    components = []
    if text:
        components.append(html.Div(text, className="select-dropdown-text"))
    components.append(
        dcc.Dropdown(id=id_, placeholder=placeholder, style={"width": size}, multi=True)
    )
    return html.Div(className="select-dropdown", children=components)
