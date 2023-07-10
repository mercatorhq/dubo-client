import pandas as pd
from dubo import ask, chart

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
housing_buyers_df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "Dennis", "Eve"],
        "house_age_max": [5, 10, 15, 20, 100],
    }
)
housing_df = pd.read_csv(
    "https://raw.githubusercontent.com/ajduberstein/geo_datasets/master/housing.csv"
)


def test_ask():
    TEST_TABLE = [
        ("What is the sum of A?", [(6,)]),
        ("What is the sum of a?", [(6,)]),
    ]

    for query, expected in TEST_TABLE:
        assert ask(query, df, rtype=list) == expected


def test_ask_multi():
    TEST_TABLE = [
        ("How many houses are available to Bob based on his preferences?", [(110,)]),
    ]
    for query, expected in TEST_TABLE:
        assert (
            ask(query, [housing_buyers_df, housing_df], rtype=list) == expected
        ), query


def test_chart():
    assert chart("Map the houses", housing_df) == "Map the houses"
    assert (
        chart(
            "What's the relationship between price and MRT distance?",
            housing_df,
        )
        == "Map the houses"
    )
