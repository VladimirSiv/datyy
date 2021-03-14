import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from faker import Faker

fake = Faker()


def simple_step_slider(id_):
    """Generates simple step slider component

    Args:
        id_ (str): Component id

    Returns:
        obj: Html div object

    """
    values = np.arange(
        np.random.randint(1, 5), np.random.randint(20, 30), np.random.randint(3, 5)
    )
    marks = {str(k): fake.word()[:5] for k in values}
    return html.Div(
        className="main-card",
        children=[
            dcc.Slider(
                id=id_,
                min=values[0],
                max=values[-1],
                step=None,
                marks=marks,
                value=5,
            )
        ],
    )
