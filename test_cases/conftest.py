import pytest
from utils.request_util import RequestUtil

@pytest.fixture(scope="class")
def api():
    return RequestUtil()