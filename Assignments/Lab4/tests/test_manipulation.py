import pytest

from pprint import pprint
from pygraph import Graph


def test_init_graph():
    graph = Graph(edges=[(1, 2)], directed=True)
    assert graph.has_node(1)
    assert graph.has_node(2)
    assert graph.has_edge((1, 2))
    pprint(graph)

    graph = Graph(edges=[(1, 2)], directed=False)
    assert graph.has_node(1)
    assert graph.has_node(2)
    assert graph.has_edge((1, 2))
    assert graph.has_edge((2, 1))
    pprint(graph)


def test_add_node(trivial: Graph):
    trivial.add_node(1)
    assert trivial.has_node(1)
    pprint(trivial)


def test_add_edge(trivial: Graph, small_directed: Graph):
    trivial.add_edge((1, 2))
    trivial.add_edge((3, 4))
    for i in range(1, 5):
        assert trivial.has_node(i)
    assert trivial.has_edge((1, 2))
    assert trivial.has_edge((3, 4))
    pprint(trivial)

    small_directed.add_edge(("d", "b"))
    assert small_directed.has_edge(("d", "b"))
    assert small_directed.has_edge(("b", "d"))
    pprint(small_directed)


def test_remove_node(trivial: Graph, small_directed: Graph, small_undirected: Graph):
    with pytest.raises(ValueError):
        trivial.remove_node("a")

    small_directed.remove_node("b")
    assert not small_directed.has_node("b")
    assert not small_directed.has_edge(("a", "b"))
    assert not small_directed.has_edge(("b", "c"))
    assert not small_directed.has_edge(("b", "d"))
    assert small_directed.has_node("a")
    assert small_directed.has_node("c")
    assert small_directed.has_node("d")
    assert small_directed.has_edge(("c", "d"))
    pprint(small_directed)

    small_undirected.remove_node("b")
    assert not small_undirected.has_node("b")
    assert not small_undirected.has_edge(("a", "b"))
    assert not small_undirected.has_edge(("b", "a"))
    assert not small_undirected.has_edge(("b", "c"))
    assert not small_undirected.has_edge(("c", "b"))
    assert not small_undirected.has_edge(("b", "d"))
    assert not small_undirected.has_edge(("d", "b"))
    assert small_undirected.has_node("a")
    assert small_undirected.has_node("c")
    assert small_undirected.has_node("d")
    assert small_undirected.has_edge(("c", "d"))
    assert small_undirected.has_edge(("d", "c"))
    pprint(small_undirected)


def test_remove_edge(trivial: Graph, small_directed: Graph, small_undirected: Graph):
    with pytest.raises(ValueError):
        trivial.remove_edge(("a", "b"))

    small_directed.add_edge(("c", "b"))
    small_directed.remove_edge(("b", "c"))
    assert small_directed.has_node("b") and small_directed.has_node("c")
    assert not small_directed.has_edge(("b", "c"))
    assert small_directed.has_edge(("c", "b"))
    pprint(small_directed)

    small_undirected.remove_edge(("b", "c"))
    assert small_undirected.has_node("b") and small_directed.has_node("c")
    assert not small_undirected.has_edge(("b", "c"))
    assert not small_undirected.has_edge(("c", "b"))
    pprint(small_undirected)
