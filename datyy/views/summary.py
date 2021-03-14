import dash_bootstrap_components as dbc
import dash_html_components as html
from server import app
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from components.cards import rate_info_card
from components.bar_charts import simple_bar_chart
from components.pie_charts import simple_pie_chart
from components.line_charts import (
    line_graph_with_radio_items,
    line_graph_trend_section,
)

from components.tables import simple_table
from logic.bar_charts import simple_bar_chart_logic
from logic.pie_charts import (
    simple_pie_chart_logic,
    simple_ring_chart_logic,
)
from logic.line_charts import (
    multiline_graph_logic,
    trend_graph_logic,
    filled_graph_logic,
    error_brands_graph_logic,
)
from logic.tables import generate_top_ares_data

layout = html.Div(
    children=[
        html.Div(
            className="main-row",
            children=[html.H3(className="title-bold pb-4", children=["Weekly Summary"])],
        ),
        dbc.Row(
            [
                dbc.Col(
                    rate_info_card(
                        "Value", "$2,750", "0.3%", "up", "fa fa-dollar-sign icon-grey"
                    )
                ),
                dbc.Col(
                    rate_info_card(
                        "Hours", "563.2", "10.1%", "down", "fa fa-hourglass icon-grey"
                    )
                ),
                dbc.Col(
                    rate_info_card(
                        "Exit %",
                        "43.5%",
                        "1.3%",
                        "up",
                        "fa fa-external-link-alt icon-grey",
                    )
                ),
                dbc.Col(
                    rate_info_card(
                        "Avg. Time", "2:25", "5.2%", "down", "fa fa-clock icon-grey"
                    )
                ),
                dbc.Col(
                    rate_info_card(
                        "Orders", "552", "15.8%", "up", "fa fa-suitcase icon-grey"
                    )
                ),
                dbc.Col(
                    rate_info_card(
                        "Expenses",
                        "1,452",
                        "20.1%",
                        "down",
                        "fa fa-dollar-sign icon-grey",
                    )
                ),
            ]
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    simple_bar_chart(
                        id_="summary-weekly-bar-chart", title="Sales per Product"
                    ),
                    width=6,
                ),
                dbc.Col(
                    simple_pie_chart("summary-active-groups", "Active Groups"),
                    width=3,
                ),
                dbc.Col(
                    simple_pie_chart("summary-top-5-products", "Top 5 Products"),
                    width=3,
                ),
            ],
            align="center",
        ),
        html.Div(
            className="main-row",
            children=[html.H3(className="title-bold", children=["Services"])],
        ),
        dbc.Row(
            className="main-row",
            children=[dbc.Col(children=[line_graph_with_radio_items()])],
        ),
        html.Div(
            className="main-row",
            children=[html.H3(className="title-bold", children=["Social metrics"])],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    simple_table(
                        id_="summary-top-areas",
                        title="Top 20 Selling Areas",
                        columns=["Country", "City", "Population", "Unit", "Amount"],
                    ),
                    width=7,
                ),
                dbc.Col(
                    [
                        line_graph_trend_section("summary-trend-likes", "Likes"),
                        line_graph_trend_section("summary-trend-comments", "Comments"),
                        line_graph_trend_section("summary-trend-followers", "Followers"),
                        line_graph_trend_section("summary-trend-views", "Views"),
                    ],
                    width=5,
                ),
            ],
        ),
    ]
)


@app.callback(Output("summary-weekly-bar-chart", "figure"), Input("url", "pathname"))
def display_summary_weekly_bar_chart(pathname):
    """Displays summary weekly bar chart

    Args:
        pathname (str): Url pathname

    Returns:
        obj: Bar chart figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return simple_bar_chart_logic()
    raise PreventUpdate


@app.callback(Output("summary-active-groups", "figure"), Input("url", "pathname"))
def display_active_groups_chart(pathname):
    """Displays active groups chart

    Args:
        pathname (str): Url pathname

    Returns:
        obj: Pie chart figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return simple_pie_chart_logic()
    raise PreventUpdate


@app.callback(Output("summary-top-5-products", "figure"), Input("url", "pathname"))
def display_top_5_products(pathname):
    """Displays top 5 products chart

    Args:
        pathname (str): Url pathname

    Returns:
        obj: Pie chart figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return simple_ring_chart_logic()
    raise PreventUpdate


@app.callback(Output("radioitems-input", "value"), Input("url", "pathname"))
def set_radio_item_service_calls(pathname):
    """Sets service calls radio items

    Args:
        pathname (str): Url pathname

    Returns:
        int: Selected radio item value

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return 1
    raise PreventUpdate


@app.callback(
    Output("summary-service-calls-graph", "figure"), Input("radioitems-input", "value")
)
def display_service_calls_graph(value):
    """Displays service calls graph based on selected
    radio item value

    Args:
        value (int): Selected radio item value

    Returns:
        obj: Graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value == 1:
        return multiline_graph_logic(4)
    if value == 2:
        return filled_graph_logic(3)
    if value == 3:
        return error_brands_graph_logic()
    raise PreventUpdate


@app.callback(Output("summary-top-areas", "data"), Input("url", "pathname"))
def set_top_areas_tables(pathname):
    """Sets top areas table data

    Args:
        pathname (str): Url pathname

    Returns:
        obj: Table data

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return generate_top_ares_data()
    raise PreventUpdate


@app.callback(
    Output("summary-trend-likes", "figure"),
    Output("summary-trend-comments", "figure"),
    Output("summary-trend-followers", "figure"),
    Output("summary-trend-views", "figure"),
    Input("url", "pathname"),
)
def display_trends(pathname):
    """Displays trend graphs

    Args:
        pathname (str): Url pathname

    Returns:
        obj: Summary likes graph figure
        obj: Summary comments graph figure
        obj: Summary followers graph figure
        obj: Summary views graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return (
            trend_graph_logic(),
            trend_graph_logic(),
            trend_graph_logic(),
            trend_graph_logic(),
        )
    raise PreventUpdate
