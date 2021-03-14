#!/usr/bin/env python

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask_login import current_user
from server import app
from views import summary, orders, products, projects, support, page_404
from components.sidebar import sidebar
from components.navbar import navbar


content = html.Div(id="page-content", className="content-sidebar-active")

app.layout = html.Div(
    [
        dcc.Store(id="side_click"),
        dcc.Store(id="orders-date", storage_type="local"),
        dcc.Store(id="product-item", storage_type="local"),
        dcc.Store(id="project-item", storage_type="local"),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
    ],
)


# Sidebar Hide/Show


@app.callback(
    [
        Output("sidebar", "className"),
        Output("page-content", "className"),
        Output("side_click", "data"),
        Output("btn_sidebar", "children"),
    ],
    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ],
)
def toggle_sidebar(click, state):
    """Toggles sidebar based on click and the state of the sidebar

    Args:
        click (int): Click
        state (str): Sidebar state

    Returns:
        str: Sidebar css className
        str: Content css className
        str: Sidebar state
        str: Button text
    """
    if click:
        if state == "SHOW":
            sidebar_class_name = "sidebar-hidden"
            content_class_name = "content-sidebar-hidden"
            cur_nclick = "HIDDEN"
            btn_label = ">"
        else:
            sidebar_class_name = "sidebar-active"
            content_class_name = "content-sidebar-active"
            cur_nclick = "SHOW"
            btn_label = "<"
    else:
        sidebar_class_name = "sidebar-active"
        content_class_name = "content-sidebar-active"
        cur_nclick = "SHOW"
        btn_label = "<"

    return sidebar_class_name, content_class_name, cur_nclick, btn_label


# Sidebar toggle submenu


@app.callback(
    Output("submenu-collapse", "is_open"),
    [Input("submenu", "n_clicks")],
    [State("submenu-collapse", "is_open")],
)
def toggle_collapse(click, is_open):
    """Toggles collapse based on click and its state

    Args:
        click (int): Click
        is_open (bool): Is submenu open

    Returns:
        bool: Submenu state

    """
    if click:
        return not is_open
    return is_open


@app.callback(Output("submenu", "className"), [Input("submenu-collapse", "is_open")])
def set_navitem_class(is_open):
    """Sets navitem class based on submenu state

    Args:
        is_open (bool): Is submenu open

    Returns:
        str: Submenu css className

    """
    if is_open:
        return "open"
    return ""


# Sidebar nav active menu item


@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    """Toggles active menu links based on url pathname

    Args:
        pathname (str): Url pathname

    Returns:
        bool: Active state for each page

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return True, False, False, False, False
    if pathname == "/datyy/orders":
        return False, True, False, False, False
    if pathname == "/datyy/products":
        return False, False, True, False, False
    if pathname == "/datyy/projects":
        return False, False, False, True, False
    if pathname == "/datyy/support":
        return False, False, False, False, True
    return False, True, False, False, False


# Routing


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    """Renders page based on url pathname

    Args:
        pathname (str): Url pathname

    Returns:
        obj: Html div layout component

    """
    if pathname in ["/datyy/", "/datyy/summary"]:
        return summary.layout
    if pathname == "/datyy/orders":
        return orders.layout
    if pathname == "/datyy/products":
        return products.layout
    if pathname == "/datyy/projects":
        return projects.layout
    if pathname == "/datyy/support":
        return support.layout
    return page_404.layout


# Navbar current user


@app.callback(Output("username", "children"), [Input("page-content", "children")])
def display_current_user_message(page):
    """Displays current user message

    Arguments:
        page (obj): Page content

    Returns:
        str: Welcoming message

    """
    if page and current_user.is_authenticated:
        return html.Div(
            children=["Welcome " + current_user.username], className="nav-username"
        )
    return ""


server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
