import pytest
from pygraph import Graph


def test_indegree(small_directed: Graph, small_undirected: Graph):
    assert small_undirected.indegree("a") == 1
    assert small_undirected.indegree("b") == 3
    assert small_undirected.indegree("c") == 2
    assert small_undirected.indegree("d") == 2

    with pytest.raises(ValueError):
        small_undirected.indegree("e")

    assert small_directed.indegree("a") == 0
    assert small_directed.indegree("b") == 1
    assert small_directed.indegree("c") == 1
    assert small_directed.indegree("d") == 2

    with pytest.raises(ValueError):
        small_directed.indegree("e")


def test_outdegree(small_directed: Graph, small_undirected: Graph):
    assert small_undirected.outdegree("a") == 1
    assert small_undirected.outdegree("b") == 3
    assert small_undirected.outdegree("c") == 2
    assert small_undirected.outdegree("d") == 2

    with pytest.raises(ValueError):
        small_undirected.indegree("e")

    assert small_directed.outdegree("a") == 1
    assert small_directed.outdegree("b") == 2
    assert small_directed.outdegree("c") == 1
    assert small_directed.outdegree("d") == 0

    with pytest.raises(ValueError):
        small_directed.indegree("e")
