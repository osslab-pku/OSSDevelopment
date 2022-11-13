import pytest

from pygraph import Graph


@pytest.fixture(scope="function")
def trivial():
    return Graph([])


@pytest.fixture(scope="function")
def small_directed():
    return Graph([("a", "b"), ("b", "c"), ("b", "d"), ("c", "d")], directed=True)


@pytest.fixture(scope="function")
def small_undirected():
    return Graph([("a", "b"), ("b", "c"), ("b", "d"), ("c", "d")], directed=False)
