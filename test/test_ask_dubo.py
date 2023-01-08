import pandas as pd
from dubo import ask

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
housing_buyers_df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "Dennis", "Eve"],
        "min_preference_for_house_age": [0, 0, 0, 0, 20],
        "max_preference_for_house_age": [5, 10, 15, 20, 100],
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
        assert ask(query, df) == expected


def test_ask_multi():
    TEST_TABLE = [
        (
            "Which buyers are interested in houses between 5 and 10 years old?",
            [("Bob",)],
        ),
        ("How many houses are available to Bob based on his preferences?", [(10,)]),
    ]
    for query, expected in TEST_TABLE:
        assert ask(query, [housing_buyers_df, housing_df]) == expected
