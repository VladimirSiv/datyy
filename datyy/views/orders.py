from datetime import datetime
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from server import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from components.calendar_heatmap import calendar_heatmap
from components.select_date import select_date
from components.bubble_charts import simple_bubble_chart
from components.titles import title_with_tooltip
from components.map_charts import simple_map_graph
from components.bar_charts import simple_bar_chart
from components.tables import pagination_table
from logic.calendar_heatmap import calendar_heatmap_logic
from logic.bubble_charts import simple_bubble_chart_logic
from logic.map_charts import simple_map_graph_logic
from logic.bar_charts import horizontal_bar_chart_logic
from logic.tables import generate_order_details_data

# Backend paging, sorting etc.
order_details = generate_order_details_data()

layout = html.Div(
    children=[
        html.Div(id="orders-date-hidden", style={"display": "none"}),
        title_with_tooltip(
            "Orders", "Click on a calendar date to select a day", "order-title", "mb-4"
        ),
        calendar_heatmap(id_="calendar-heatmap", title="Orders per day"),
        select_date(
            id_="orders-date-select",
            date_min=datetime(2019, 1, 1),
            date_max=datetime(2020, 12, 31),
            text="Pick a date: ",
        ),
        dbc.Row(
            [
                dbc.Col(simple_map_graph("orders-map", "Orders per state"), width=6),
                dbc.Col(
                    simple_bar_chart(
                        id_="orders-same-day-delivery",
                        title="Orders Same-Day Delivery",
                    ),
                    width=6,
                ),
            ]
        ),
        simple_bubble_chart(id_="orders-per-states", title="Orders per product"),
        pagination_table(
            id_="order-details-table",
            title="Orders in detail",
            columns=[
                "Product",
                "Date",
                "Time",
                "Country",
                "City",
                "Delivered",
                "Delivery Time",
                "Amount",
                "Unit",
            ],
        ),
    ]
)


@app.callback(
    [Output("calendar-heatmap", "figure"), Output("orders-date-hidden", "children")],
    [Input("url", "pathname")],
    [State("orders-date", "data")],
)
def display_calendar_heatmap(pathname, orders_date):
    """Displays calendar heatmap

    Args:
        pathname (str): Url pathname
        orders_date (str): State of orders date

    Returns:
        obj: Heatmap figure
        str: Orders date

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname == "/datyy/orders":
        date = orders_date
        if orders_date is None:
            date = datetime(2019, 1, 1).strftime("%Y-%m-%d")
        return calendar_heatmap_logic(), date
    raise PreventUpdate


@app.callback(
    [Output("orders-date", "data"), Output("orders-date-select", "date")],
    [
        Input("orders-date-hidden", "children"),
        Input("calendar-heatmap", "clickData"),
        Input("orders-date-select", "date"),
    ],
)
def set_orders_date_select_hidden(hidden_value, calendar_date, orders_date_selected):
    """Sets orders date for state and hidden div

    Args:
        hidden_value (str): Value stored in hidden div
        calendar_date (str): Calendar date
        orders_date_selected (str): Selected date

    Returns:
        str: State value
        str: Select value

    Raises:
        PreventUpdate: if arguments are not valid

    Note:
        This callback, among other things, takes care of
        application state and stores selected date

    """
    ctx = dash.callback_context
    if not ctx.triggered:
        input_id = None
    else:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "orders-date-hidden" and hidden_value:
        return hidden_value, datetime.strptime(hidden_value, "%Y-%m-%d")
    if input_id == "calendar-heatmap" and calendar_date:
        date = calendar_date["points"][0]["text"].split(" : ")[0]
        return date, datetime.strptime(date, "%Y-%m-%d")
    if input_id == "orders-date-select" and orders_date_selected:
        return orders_date_selected, orders_date_selected
    raise PreventUpdate


@app.callback(Output("orders-per-states", "figure"), Input("orders-date-select", "date"))
def display_orders_bubble_graph(date):
    """Displays orders bubble graph

    Args:
        date (str): Selected date

    Returns:
        obj: Bubble chart figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if date:
        return simple_bubble_chart_logic()
    raise PreventUpdate


@app.callback(Output("orders-map", "figure"), Input("orders-date-select", "date"))
def display_orders_per_state(date):
    """Displays orders per state graph

    Args:
        date (str): Selected date

    Returns:
        obj: Graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if date:
        return simple_map_graph_logic()
    raise PreventUpdate


@app.callback(
    Output("orders-same-day-delivery", "figure"), Input("orders-date-select", "date")
)
def display_orders_same_day_delivery(date):
    """Displays orders same day delivery graph

    Args:
        date (str): Selected date

    Returns:
        obj: Graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if date:
        return horizontal_bar_chart_logic()
    raise PreventUpdate


@app.callback(
    Output("order-details-table", "data"),
    Input("order-details-table", "page_current"),
    Input("order-details-table", "page_size"),
    Input("order-details-table", "sort_by"),
)
def set_orders_daily_details_table_data(page_current, page_size, sort_by):
    """Sets orders daily details table data

    Args:
        page_current (int): Current pagination page
        page_size (int): Page size
        sort_by (list): Sort by columns

    Returns:
        obj: Table data

    """
    if len(sort_by):
        df_sorted = order_details.sort_values(
            sort_by[0]["column_id"],
            ascending=sort_by[0]["direction"] == "asc",
            inplace=False,
        )
    else:
        df_sorted = order_details
    return df_sorted.iloc[
        page_current * page_size : (page_current + 1) * page_size
    ].to_dict("records")
