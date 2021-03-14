import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
from server import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from components.dropdowns import dropdown_single, dropdown_multiple
from components.titles import title_with_tooltip
from components.cards import bootstrap_card_with_icon
from components.line_charts import line_graph_with_title
from components.sliders import simple_step_slider
from components.networks import network_graph
from logic.dropdowns import dropdown_single_logic
from logic.line_charts import (
    multiline_graph_logic,
    filled_graph_logic,
)
from logic.networks import network_graph_logic
from logic.bar_charts import multi_group_bar_chart


layout = html.Div(
    children=[
        html.Div(id="product-item-temp", style={"display": "none"}),
        title_with_tooltip(
            "Details",
            "Select product to see its history",
            "products-single-title",
            "mb-4",
        ),
        dbc.Row(
            dbc.Col(
                dropdown_single(
                    id_="product-item-select",
                    placeholder="Select Product",
                    text="Product:",
                ),
                width=3,
            ),
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    bootstrap_card_with_icon(
                        id_="product-info-sold",
                        title="sold",
                        icon="fas fa-dollar-sign",
                    )
                ),
                dbc.Col(
                    bootstrap_card_with_icon(
                        id_="product-info-produced",
                        title="produced",
                        icon="fas fa-industry",
                    )
                ),
                dbc.Col(
                    bootstrap_card_with_icon(
                        id_="product-info-in-store",
                        title="store",
                        icon="fas fa-store",
                    )
                ),
                dbc.Col(
                    bootstrap_card_with_icon(
                        id_="product-info-delivered",
                        title="delivered",
                        icon="fas fa-truck",
                    )
                ),
                dbc.Col(
                    bootstrap_card_with_icon(
                        id_="product-info-sameday-delivered",
                        title="same-day",
                        icon="fas fa-shipping-fast",
                    )
                ),
            ],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    line_graph_with_title(id_="product-line-graph", title="Orders"),
                    width=6,
                ),
                dbc.Col(
                    line_graph_with_title(
                        id_="product-bar-chart", title="Same-day Delivery"
                    ),
                    width=6,
                ),
            ],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    simple_step_slider(id_="product-slider"),
                    width={"offset": 3, "size": 6},
                )
            ],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    network_graph(id_="product-network-graph", title="Related products"),
                    width={"offset": 2, "size": 8},
                )
            ],
        ),
        title_with_tooltip(
            "Compare",
            "Select multiple products to compare them",
            "products-compare-title",
            "mb-4",
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    dropdown_multiple(
                        id_="product-item-multi-select",
                        placeholder="Select Products",
                        text="Products",
                        size="800px",
                    ),
                )
            ],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    line_graph_with_title(
                        id_="product-compare-line-graph",
                        title="Orders",
                        default_fig=True,
                        default_fig_text="Please select products to compare",
                    ),
                    width=6,
                ),
                dbc.Col(
                    line_graph_with_title(
                        id_="product-compare-bar-chart",
                        title="Same-day Delivery",
                        default_fig=True,
                        default_fig_text="Please select products to compare",
                    ),
                    width=6,
                ),
            ],
        ),
    ]
)


@app.callback(
    [Output("product-item-select", "options"), Output("product-item-temp", "children")],
    [Input("url", "pathname")],
    [State("product-item", "data")],
)
def set_product_select_item_options(pathname, product_stored):
    """Sets product select options

    Args:
        pathname (str): Url pathname
        product_stored (str): Product state value

    Returns:
        list: List of product options
        str: Product state value

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname == "/datyy/products":
        product_item = product_stored
        if product_stored is None:
            product_item = 0
        return dropdown_single_logic(), product_item
    raise PreventUpdate


@app.callback(
    [Output("product-item", "data"), Output("product-item-select", "value")],
    [
        Input("product-item-temp", "children"),
        Input("product-item-select", "value"),
    ],
)
def set_hidden_product_item(hidden, dropdown_value):
    """Sets hidden and selected product item

    Args:
        hidden (str): Hidden product value
        dropdown_value (str): Selected product value

    Returns:
        str: Product state value
        str: Selected product value

    Raises:
        PreventUpdate: if arguments are not valid

    """
    ctx = dash.callback_context
    if not ctx.triggered:
        input_id = None
    else:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "product-item-temp" and hidden is not None:
        return hidden, int(hidden)
    if input_id == "product-item-select" and dropdown_value is not None:
        return dropdown_value, dropdown_value
    raise PreventUpdate


@app.callback(
    [
        Output("product-info-sold", "children"),
        Output("product-info-produced", "children"),
        Output("product-info-in-store", "children"),
        Output("product-info-delivered", "children"),
        Output("product-info-sameday-delivered", "children"),
    ],
    [Input("product-item-select", "value")],
)
def set_product_info_values(value):
    """Sets product information values

    Args:
        value: Selected product item

    Returns:
        list: List of product information values

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value is not None:
        values = list(np.random.randint(1000, 10000, size=4))
        values.append(str(np.random.randint(10, 100)) + "%")
        return values
    raise PreventUpdate


@app.callback(
    [
        Output("product-line-graph", "figure"),
        Output("product-bar-chart", "figure"),
        Output("product-network-graph", "figure"),
    ],
    [Input("product-item-select", "value"), Input("product-slider", "value")],
)
def display_product_line_graph(value, slider):
    """Displays product line graph

    Args:
        value: Selected product item
        slider: Selected slider value

    Returns:
        obj: Product line graph figure
        obj: Product bar chart figure
        obj: Product network graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value or slider:
        return (
            filled_graph_logic(1),
            multiline_graph_logic(3, dashed_lines=True),
            network_graph_logic(),
        )
    raise PreventUpdate


@app.callback(
    [Output("product-item-multi-select", "options")], [Input("url", "pathname")]
)
def set_product_multi_select_options(pathname):
    """Sets product multi select options

    Args:
        pathname (str): Url pathname

    Returns:
        list: List of options

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname == "/datyy/products":
        return [dropdown_single_logic()]
    raise PreventUpdate


@app.callback(
    [
        Output("product-compare-line-graph", "figure"),
        Output("product-compare-bar-chart", "figure"),
    ],
    Input("product-item-multi-select", "value"),
    State("product-item-multi-select", "options"),
)
def display_compare_products_graphs(values, options):
    """Displays compare products graphs

    Args:
        values (list): List of product selected
        options (list): List of options

    Returns:
        obj: Multiline graph figure
        obj: Multigroup bar chart figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if values and options:
        return (
            multiline_graph_logic(len(values), options=options, values=values),
            multi_group_bar_chart(len(values), options=options, values=values),
        )
    raise PreventUpdate
