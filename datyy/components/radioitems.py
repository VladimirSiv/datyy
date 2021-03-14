import dash_bootstrap_components as dbc
import dash_html_components as html
from faker import Faker

fake = Faker()


def radio_items(id_, num):
    """Generates radio items component

    Args:
        id_ (str): Component id
        num (int): Radio items

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="radio-items",
        children=[
            dbc.Form(
                dbc.FormGroup(
                    dbc.RadioItems(
                        options=[
                            {"label": fake.word(), "value": i} for i in range(1, num + 1)
                        ],
                        inline=True,
                        id=id_,
                    ),
                )
            )
        ],
    )
