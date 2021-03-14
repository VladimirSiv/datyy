import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
from server import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from components.cards import simple_info_card
from components.dropdowns import dropdown_single
from components.cards import project_info_card
from components.tables import simple_table
from components.gantts import simple_gantt_graph
from logic.dropdowns import dropdown_single_logic
from logic.tables import generate_project_tasks_data
from logic.pie_charts import sunburst_chart_logic
from logic.gantts import simple_gantt_logic


layout = html.Div(
    children=[
        html.Div(id="project-temp", style={"display": "none"}),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    dropdown_single(
                        id_="project-select",
                        placeholder="Select Project",
                        text="Project:",
                    ),
                    width=3,
                ),
            ],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    simple_info_card(
                        id_="project-card-planning",
                        title="Planning",
                    )
                ),
                dbc.Col(
                    simple_info_card(
                        id_="project-card-design",
                        title="Design",
                    )
                ),
                dbc.Col(
                    simple_info_card(
                        id_="project-card-development",
                        title="Development",
                    )
                ),
                dbc.Col(
                    simple_info_card(
                        id_="project-card-testing",
                        title="Testing",
                    )
                ),
                dbc.Col(
                    simple_info_card(
                        id_="project-card-cost",
                        title="Cost",
                    )
                ),
                dbc.Col(
                    simple_info_card(
                        id_="project-card-duration",
                        title="Duration",
                    )
                ),
            ],
        ),
        dbc.Row(
            className="main-row",
            children=[
                dbc.Col(
                    project_info_card(
                        id_="budget-graph",
                        title="Budget spending",
                        subcomponents={
                            "project-budget": "Budget",
                            "project-remaining": "Remaining",
                            "project-currently": "Currently",
                        },
                    ),
                    width=6,
                ),
                dbc.Col(
                    simple_table(
                        id_="project-tasks-table",
                        title="Overdue tasks",
                        columns=[
                            "Overdue (days)",
                            "Task",
                            "Deadline",
                            "Employee",
                        ],
                    ),
                    width=6,
                ),
            ],
        ),
        html.Div(
            className="main-row", children=[html.H4("Milestones", className="title-bold")]
        ),
        dbc.Row(
            className="main-row",
            children=[dbc.Col(simple_gantt_graph(id_="project-gantt-graph"))],
        ),
    ]
)


@app.callback(
    [Output("project-select", "options"), Output("project-temp", "children")],
    Input("url", "pathname"),
    State("project-item", "data"),
)
def set_project_select_options(pathname, project_stored):
    """Sets project select options

    Args:
        pathname (str): Url pathname
        project_stored (str): State of project value

    Returns:
        list: List of options
        str: Project hidden value

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if pathname == "/datyy/projects":
        project = project_stored
        if project_stored is None:
            project = 0
        return dropdown_single_logic(), project
    raise PreventUpdate


@app.callback(
    [Output("project-item", "data"), Output("project-select", "value")],
    [Input("project-temp", "children"), Input("project-select", "value")],
)
def set_hidden_project_item(hidden, dropdown_value):
    """Set state and selected project value

    Args:
        hidden (str): Hidden project value
        dropdown_value (str): Selected project value

    Returns:
        str: State of project value
        str: Selected project value

    Raises:
        PreventUpdate: if arguments are not valid

    """
    ctx = dash.callback_context
    if not ctx.triggered:
        input_id = None
    else:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "project-temp" and hidden is not None:
        return hidden, int(hidden)
    if input_id == "project-select" and dropdown_value is not None:
        return dropdown_value, dropdown_value
    raise PreventUpdate


@app.callback(
    [
        Output("project-card-" + card_type, "children")
        for card_type in [
            "planning",
            "design",
            "development",
            "testing",
            "cost",
            "duration",
        ]
    ],
    Input("project-select", "value"),
)
def set_project_card_info_values(value):
    """Sets project information values

    Args:
        value (str): Selected project value

    Returns:
        str: Project planning value
        str: Project design value
        str: Project development value
        str: Project testing value
        str: Project cost value
        str: Project duration value

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value is not None:
        result = [str(x) + "%" for x in np.random.randint(100, size=4)]
        result.append("$" + str(np.random.randint(100, 1000)))
        result.append(str(np.random.randint(10, 20)) + " days")
        return result
    raise PreventUpdate


@app.callback(Output("project-tasks-table", "data"), Input("project-select", "value"))
def set_project_tasks_table(value):
    """Sets project tasks table data

    Args:
        value (str): Select project value

    Returns:
        obj: Table data

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value is not None:
        return generate_project_tasks_data()
    raise PreventUpdate


@app.callback(
    [
        Output("project-budget", "children"),
        Output("project-remaining", "children"),
        Output("project-currently", "children"),
        Output("budget-graph", "figure"),
    ],
    Input("project-select", "value"),
)
def set_project_budget_info(value):
    """Sets project budget information

    Args:
        value (str): Selected project value

    Returns:
        str: Project budget value
        str: Project remaining value
        str: Project currently value
        obj: Project Budget graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value is not None:
        result = list(np.random.randint(0, 1000, size=3))
        result.append(sunburst_chart_logic())
        return result
    raise PreventUpdate


@app.callback(Output("project-gantt-graph", "figure"), Input("project-select", "value"))
def display_gantt_graph(value):
    """Displays gantt graph figure

    Args:
        value (str): Selected project value

    Returns:
        obj: Project gantt graph figure

    Raises:
        PreventUpdate: if arguments are not valid

    """
    if value is not None:
        return simple_gantt_logic()
    raise PreventUpdate
