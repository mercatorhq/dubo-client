import os
from dotenv import load_dotenv
import pytest

load_dotenv(".env")


@pytest.fixture
def dubo_test_key():
    return os.environ.get("DUBO_TEST_KEY", None)
