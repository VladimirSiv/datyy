from faker import Faker

fake = Faker()


def dropdown_single_logic():
    """Generates dropdown options

    Returns:
        list: List of options as dicts

    Note:
        This is constant, on purpose, to show how to perserve
        a state of an application. In real setting, this would
        be an API call i.e. values would be easily realted to values
        and restored from the state

    """
    return [
        {"label": "clumsy", "value": 0},
        {"label": "wealthy", "value": 1},
        {"label": "strong", "value": 2},
        {"label": "motionless", "value": 3},
        {"label": "workable", "value": 4},
        {"label": "wrist", "value": 5},
        {"label": "yell", "value": 6},
        {"label": "silky", "value": 7},
    ]
