from datetime import datetime, timedelta, date
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from styles.graphs import (
    CAL_HEATMAP_COLORSCALE,
    CAL_HEATMAP_BACKGROUND_COLOR,
    CAL_HEATMAP_AXIS_COLOR,
)

MONTH_NAMES = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def calendar_heatmap_logic():
    """Generates calendar heatmap graph figure

    Returns:
        obj: Plotly figure

    """
    dates = _generate_dummy_dates()
    years = dates["created_at"].dt.year.unique().tolist()
    fig = make_subplots(rows=len(years), cols=1, subplot_titles=[str(x) for x in years])
    for i, year in enumerate(years):
        data = dates[
            dates["created_at"].between(
                datetime(year, 1, 1, 0, 0, 0),
                datetime(year + 1, 1, 1, 0, 0, 0),
            )
        ]
        create_cal_heatmap_fig(year, data, fig, i)
        fig.update_layout(height=250 * len(years))
    return fig


def create_cal_heatmap_fig(year, dates, fig, row):
    """Generates single year calendar heatmap figure

    Args:
        year (int): Year
        dates (obj): Pandas DataFrame dates
        fig (obj): Main figure
        row (int): Subplot row

    Returns:
        obj: Plotly figure

    """
    month_days = [(date(year, i + 1, 1) - date(year, i, 1)).days for i in range(1, 12)]
    month_positions = (np.cumsum(month_days) - 15) / 7

    dates_in_year = _get_dates_in_a_year(year)
    df_dates_in_year = pd.DataFrame({"created_at": dates_in_year})
    weekdays_in_year = [i.weekday() for i in dates_in_year]
    weeknumber_of_dates = [i.strftime("%Gww%V")[2:] for i in dates_in_year]
    merged_dates = (
        pd.merge(df_dates_in_year, dates, how="outer", on=["created_at"])
        .fillna(0)["count"]
        .tolist()
    )
    text = [
        dates_in_year[i].strftime("%Y-%m-%d") + " : " + str(int(merged_dates[i]))
        for i in range(len(dates_in_year))
    ]

    data = [
        go.Heatmap(
            x=weeknumber_of_dates,
            y=weekdays_in_year,
            z=merged_dates,
            text=text,
            hoverinfo="text",
            xgap=3,
            ygap=3,
            colorscale=CAL_HEATMAP_COLORSCALE,
            showscale=False,
        )
    ]

    layout = go.Layout(
        height=280,
        yaxis=dict(
            showline=False,
            showgrid=False,
            zeroline=False,
            tickmode="array",
            ticktext=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            tickvals=[0, 1, 2, 3, 4, 5, 6],
        ),
        xaxis=dict(
            showline=False,
            showgrid=False,
            zeroline=False,
            tickmode="array",
            ticktext=MONTH_NAMES,
            tickvals=month_positions,
        ),
        font={"size": 10, "color": CAL_HEATMAP_AXIS_COLOR},
        paper_bgcolor=CAL_HEATMAP_BACKGROUND_COLOR,
        plot_bgcolor=CAL_HEATMAP_BACKGROUND_COLOR,
        margin=dict(t=40),
    )

    if fig is None:
        fig = go.Figure(data=data, layout=layout)
    else:
        fig.add_traces(data, rows=[(row + 1)] * len(data), cols=[1] * len(data))
        fig.update_layout(layout)
        fig.update_xaxes(layout["xaxis"])
        fig.update_yaxes(layout["yaxis"])
    return fig


def _generate_dummy_dates():
    """Helper function to generate dummy dates

    Returns:
        obj: Pandas Dataframe

    """
    start_date = datetime(2019, 1, 1)
    dates = {}
    count = 0
    while count < 715:
        count += np.random.randint(1, 5)
        tmp_date = start_date + timedelta(days=count)
        dates[tmp_date.strftime("%Y-%m-%d")] = np.random.randint(1, 200)
    dates = pd.DataFrame(dates.items(), columns=["created_at", "count"])
    dates["created_at"] = pd.to_datetime(dates["created_at"])
    return dates


def _get_dates_in_a_year(year):
    """Helper function to get dates in a year

    Args:
        year (int): Year

    Returns:
        list: List of dates in a year

    """
    year_start = datetime(year, 1, 1, 0, 0, 0)
    year_end = datetime(year + 1, 1, 1, 0, 0, 0)
    delta = year_end - year_start
    return [year_start + timedelta(days=i) for i in range(delta.days)]
