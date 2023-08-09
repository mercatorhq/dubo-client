import pandas as pd
import vcr

from dubo import ask, chart, query as dubo_query
from dubo.ask_dubo import generate_sql, search_tables
from dubo.config import get_dubo_key, set_dubo_key

myvcr = vcr.VCR(
    cassette_library_dir="test/fixtures/vcr_cassettes",
    record_mode="once",  # type: ignore
    match_on=["uri", "method"],
)

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


@myvcr.use_cassette("test_ask_dubo.yaml")  # type: ignore
def test_query(dubo_test_key):
    # MusicBrainz key
    set_dubo_key(dubo_test_key)
    assert get_dubo_key() == dubo_test_key
    # How many area types are there?
    data_result = dubo_query("How many area types are there?")
    assert data_result.results_set == [
        {"num_area_types": 9}
    ] or data_result.results_set == [{"count": 9}]


@myvcr.use_cassette("test_query_just_sql.yaml")  # type: ignore
def test_query_just_sql(dubo_test_key):
    set_dubo_key(dubo_test_key)
    sql_text = generate_sql("How many area types are there?")
    assert sql_text in (
        "SELECT COUNT(DISTINCT type) AS num_area_types FROM public.area",
        "SELECT COUNT(*) FROM public.area_type",
        "SELECT COUNT(*) AS num_area_types FROM area_types",
    )


@myvcr.use_cassette("test_query_just_tables.yaml")  # type: ignore
def test_query_just_tables(dubo_test_key):
    set_dubo_key(dubo_test_key)
    tables = search_tables("How many area types are there?")
    print(tables)
    assert any(["area_type" == table["table_name"] for table in tables])
