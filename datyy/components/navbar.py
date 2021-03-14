import dash_html_components as html
import dash_bootstrap_components as dbc
from server import app

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url("logo2.png"), height="30px")),
                    dbc.Col(dbc.NavbarBrand("Datyy", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/datyy/",
            className="nav-logo",
        ),
        dbc.Button(
            outline=False, className="sidebar-button mr-1", id="btn_sidebar", size="sm"
        ),
        html.Span(
            children=[
                html.Div(id="username", className="username text-light h3"),
                dbc.Button(
                    "Logout",
                    outline=True,
                    className="logout-button",
                    href="/logout",
                    external_link=True,
                    size="sm",
                ),
            ],
            className="nav-span ml-auto",
        ),
    ],
    color="dark",
    dark=True,
    sticky="top",
)
