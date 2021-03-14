import dash_table
import dash_html_components as html
from styles.tables import (
    TABLE_CELL_STYLE,
    TABLE_HEADER_STYLE,
    TABLE_CONDITIONAL_STYLE,
)


def simple_table(id_, title, columns):
    """Generates simple table component

    Args:
        id_ (str): Component id
        title (str): Component title
        columns (list): List of table columns

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card",
        children=[
            html.Div(
                className="title-bold title-centered",
                children=[title],
            ),
            html.Br(),
            dash_table.DataTable(
                id=id_,
                columns=[{"name": i, "id": i} for i in columns],
                style_cell=TABLE_CELL_STYLE,
                style_data_conditional=TABLE_CONDITIONAL_STYLE,
                style_header=TABLE_HEADER_STYLE,
                style_as_list_view=True,
            ),
        ],
    )


def pagination_table(id_, title, columns):
    """Generates pagination table component

    Args:
        id_ (str): Component id
        title (str): Component title
        columns (list): List of table columns

    Returns:
        obj: Html div object

    """
    return html.Div(
        className="main-card table-paggination-padding",
        children=[
            html.Div(
                className="title-bold title-centered",
                children=[title],
            ),
            html.Br(),
            dash_table.DataTable(
                id=id_,
                page_current=0,
                page_size=15,
                page_action="custom",
                sort_action="custom",
                sort_mode="single",
                sort_by=[],
                columns=[{"name": i, "id": i} for i in columns],
                style_cell=TABLE_CELL_STYLE,
                style_data_conditional=TABLE_CONDITIONAL_STYLE,
                style_header=TABLE_HEADER_STYLE,
                style_as_list_view=True,
            ),
        ],
    )
