import dash_html_components as html
from server import app


layout = html.Div(
    className="pt-4 fill-page-content page-centered",
    children=[
        html.H1("Ooopss!"),
        html.P("Empty on purpose. Sorry..."),
        html.Img(src=app.get_asset_url("under_construction.jpg"), height="500px"),
        html.A(
            "Business vector created by pikisuperstar - www.freepik.com",
            href="https://www.freepik.com/vectors/business",
            style={"font-size": "10px"},
        ),
    ],
)
