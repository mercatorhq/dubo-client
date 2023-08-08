import pandas as pd
from dubo import ask, chart, query as dubo_query
from dubo.config import set_dubo_key

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
    ch = str(
        chart(
            "Map the houses",
            housing_df,
            specify_chart_type="DECK_GL",
            as_string=True,  # noqa: E501
        )
    )
    assert "html" in ch


def test_query(dubo_test_key):
    # MusicBrainz key
    set_dubo_key(dubo_test_key)
    # How many area types are there?
    assert dubo_query("How many area types are there?") == [(9,)]
