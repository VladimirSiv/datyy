import dash_html_components as html
import dash_bootstrap_components as dbc


def title_with_tooltip(title, tooltip_text, tooltip_target, title_class=None):
    """Generates title with tooltip component

    Args:
        title (str): Component title
        tooltip_text (str): Tooltip text
        tooltip_target (str): Tooltip target
        title_class (str, optional): Additional css classes for title

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-row",
        children=[
            html.H3(
                id=tooltip_target,
                className="title-bold " + title_class,
                children=[title],
                style={"display": "inline-block", "cursor": "pointer"},
            ),
            dbc.Tooltip(
                tooltip_text,
                target=tooltip_target,
            ),
        ],
    )
