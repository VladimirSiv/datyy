import dash_html_components as html
import dash_core_components as dcc


def simple_info_card(id_, title):
    """Generates simple info card component

    Args:
        id_ (str): Component id
        title (str): Component title

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="title-centered main-card",
        children=[
            html.H6(title, className="main-card-title"),
            html.Div(id=id_, className="main-card-value"),
        ],
    )


def rate_info_card(title, number, rate, rate_mode, icon):
    """Generates rate info card component

    Args:
        com_id (str): Component id
        com_title (str): Component title
        rate (str): Component rate
        rate_mode (str): Component rate mode
        icon (str): Component icon

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card summary-card",
        children=[
            html.Div(
                className="main-card-title-value",
                children=[
                    html.Div(
                        title,
                        className="main-card-title",
                    ),
                    html.Div(
                        className="main-card-value-rate",
                        children=[
                            html.Div(number, className="main-card-value"),
                            *_rate_section(rate, rate_mode),
                        ],
                    ),
                ],
            ),
            html.Div(
                html.I(className=icon),
            ),
        ],
    )


def project_info_card(id_, title, subcomponents):
    """Generates project info card component

    Args:
        id (str): Component id
        title (str): Component title
        subcomponents (dict): Subcomponents where keys are ids
                              and values are titles

    Returns:
        obj: Html div object

    """
    return html.Div(
        children=[
            html.Div(
                className="title-centered main-card",
                children=[
                    html.Div(
                        className="title-bold title-centered",
                        children=[title],
                    ),
                    html.Hr(),
                    html.Div(
                        children=[
                            dcc.Graph(id=id_),
                        ]
                    ),
                ],
            ),
            html.Div(
                className="project-card-info-section mb-2 title-centered",
                children=[
                    html.Div(
                        className="project-card-info main-card",
                        children=[
                            html.Div(title, className="main-card-title"),
                            html.Div(id=id_, className="main-card-value"),
                        ],
                    )
                    for id_, title in subcomponents.items()
                ],
            ),
        ]
    )


def bootstrap_card_with_icon(id_, title, icon):
    """Generates bootstrap card component

    Args:
        id_ (str): Component id
        title (str): Component title
        icon (str): Component icon

    Returns:
        obj: Html div object

    """
    return html.Div(
        html.Div(
            html.Div(
                html.Div(
                    [
                        html.Div(
                            [
                                html.I(
                                    className=icon + " icon-grey fa-2x"
                                    " font-large-2-float-left"
                                ),
                            ],
                            className="align-self-center",
                        ),
                        html.Div(
                            [
                                html.H3(id=id_, className="main-card-value"),
                                html.Span(title, className="main-card-title"),
                            ],
                            className="media-body text-right",
                        ),
                    ],
                    className="media d-flex",
                ),
                className="card-body",
            ),
            className="card-content",
        ),
        className="main-card",
    )


def _rate_section(rate, rate_mode):
    """Helper function for building rate section

    Args:
        rate (str): Rate value
        rate_mode (str): Rate mode

    Returns:
        list: List of html divs

    """
    if rate_mode == "up":
        return [
            html.Div(className="fa fa-arrow-up rate-up"),
            html.Div(rate, className="main-card-rate-up"),
        ]
    return [
        html.Div(className="fa fa-arrow-down rate-down"),
        html.Div(rate, className="main-card-rate-down"),
    ]
