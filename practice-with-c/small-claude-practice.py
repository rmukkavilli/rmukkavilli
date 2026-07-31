from typing import List, Tuple, Dict, Set

def get_direct_calls(edges: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    """
    Given a list of (caller, callee) pairs, return a dict mapping
    each caller to the set of functions it directly calls.

    Example:
        edges = [("main", "parse"), ("main", "validate"), ("parse", "tokenize")]
        get_direct_calls(edges) -> {"main": {"parse", "validate"}, "parse": {"tokenize"}}
    """
    if not edges:
        return {}
    edge_dict = {}
    for edge in edges:
        caller, callee = edge
        if caller not in edge_dict:
            edge_dict[caller] = set()
        edge_dict[caller].add(callee)
          
    return edge_dict

    
edges = [("main", "parse"), ("main", "validate"), ("main", "validate"), ("parse", "tokenize"), ("parse", "tokenize")]
print(get_direct_calls(edges))
# o/p : {"main": {"parse", "validate"}, "parse": {"tokenize"}}


def test_empty_edges():
    assert get_direct_calls([]) == {}

def test_edges_as_None():
    assert get_direct_calls(None) == {}

def test_edges_duplicates():
    assert get_direct_calls([("main", "parse"), ("main", "validate"), ("main", "validate"), ("parse", "tokenize"), ("parse", "tokenize")]) == {'main': {'parse', 'validate'}, 'parse': {'tokenize'}}
 

