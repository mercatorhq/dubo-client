import pandas as pd
from dubo import ask

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

def test_ask():
    TEST_TABLE = [
        ('What is the sum of a?', [(6,)]),
        ('What is the sum of A?', [(6,)]),
        ('What is the cross-product of a with itself?', [(6,)]),
    ]

    for query, expected in TEST_TABLE:
        assert ask(query, df) == expected
