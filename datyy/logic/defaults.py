from styles.graphs import GRAPH_BACKGROUND_COLOR, GRAPH_TEXT_COLOR


def default_figure(text):
    """Generates default graph figure

    Args:
        text (str): Figure text

    Returns:
        dict: Data for Plotly figure

    """
    return {
        "layout": {
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
            "paper_bgcolor": GRAPH_BACKGROUND_COLOR,
            "plot_bgcolor": GRAPH_BACKGROUND_COLOR,
            "annotations": [
                {
                    "text": text,
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 15, "color": GRAPH_TEXT_COLOR},
                }
            ],
        }
    }
