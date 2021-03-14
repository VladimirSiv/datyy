import dash_bootstrap_components as dbc
import dash_html_components as html

submenu = [
    html.Li(
        dbc.Row(
            className="title-centered mt-2 mb-2 main-text-primary submenu-item",
            children=[
                dbc.Col("Reports"),
                dbc.Col(html.I(className="fas fa-chevron-right mr-3"), width="auto"),
            ],
        ),
        style={"cursor": "pointer"},
        id="submenu",
    ),
    dbc.Collapse(
        [
            dbc.NavLink("Projects", href="/datyy/projects", id="page-4-link"),
            dbc.NavLink("Support", href="/datyy/support", id="page-5-link"),
        ],
        id="submenu-collapse",
    ),
]

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Summary", href="/datyy/summary", id="page-1-link"),
                dbc.NavLink("Orders", href="/datyy/orders", id="page-2-link"),
                dbc.NavLink("Products", href="/datyy/products", id="page-3-link"),
                *submenu,
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        html.Div(
            className="application-rights",
            children=[
                html.Div("Datyy - Template Dashboard"),
            ],
        ),
    ],
    id="sidebar",
    className="sidebar-active",
)
