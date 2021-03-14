import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()


def generate_top_ares_data():
    """Generates top area data

    Returns:
        dict: Table data

    """
    num = 20
    data = {
        "Country": [fake.country()[:10] for _ in range(num)],
        "City": [fake.city() for _ in range(num)],
        "Population": np.random.randint(10000, 100000, size=num),
        "Unit": [fake.word() for _ in range(num)],
        "Amount": np.random.randint(1000, size=num),
    }
    return pd.DataFrame(data).to_dict("records")


def generate_order_details_data():
    """Generates order details data

    Returns:
        obj: Pandas DataFrame object

    """
    num = 60
    delivered = [fake.boolean() for _ in range(num)]
    data = {
        "Product": [fake.word()[:10] for _ in range(num)],
        "Date": [fake.date() for _ in range(num)],
        "Time": [fake.time() for _ in range(num)],
        "Country": [fake.country()[:10] for _ in range(num)],
        "City": [fake.city() for _ in range(num)],
        "Delivered": ["Yes" if x else "No" for x in delivered],
        "Delivery Time": [fake.time() if x else "-" for x in delivered],
        "Amount": [fake.random_number() for _ in range(num)],
        "Unit": [fake.word()[:10] for _ in range(num)],
    }
    return pd.DataFrame(data)


def generate_project_tasks_data():
    """Generates project tasks data

    Returns:
        dict: Table data

    """
    num = 15
    data = {
        "Overdue (days)": np.random.randint(2, 20, size=num),
        "Task": [" ".join(fake.words(3)) for _ in range(num)],
        "Deadline": [fake.future_datetime().strftime("%Y-%m-%d") for _ in range(num)],
        "Employee": [fake.name()[:15] for _ in range(num)],
    }
    return pd.DataFrame(data).to_dict("records")
