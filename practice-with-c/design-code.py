from typing import List, Dict, Union

def parse_config(lines: List[str]) -> Dict[str, Union[str, List[str], None]]:
    """
    Given a list of raw config strings in "key=value" format, parse them into
    a dict of settings.

    - Whitespace around key and value is stripped
    - If a key appears more than once, group all its values into a list
    - A line with no "=" is malformed — stored with a marker value (your choice)

    Example:
        lines = ["timeout=30", "retries=5", "malformed_line", "  mode = auto  ", "timeout=60"]
        parse_config(lines) -> {
            "timeout": ["30", "60"],
            "retries": "5",
            "mode": "auto",
            "malformed_line": None  # or whatever marker you pick
        }
    """
    if not lines:
        return {}
    lines_dict = {}
    for line in lines:
        line = line.strip()
        if "=" not in line:
            lines_dict[line] = "INVALID"
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if key not in lines_dict:
            lines_dict[key] = value
        elif isinstance(lines_dict[key], list):
            lines_dict[key].append(value)
        else:
            lines_dict[key] = [lines_dict[key], value]
    return lines_dict
line1 =["timeout=30", "retries=5", "malformed_line", "  mode = auto  ", "timeout=60", "timeout=90"]
print(parse_config(line1))

def test_empty_line():
    assert parse_config([]) == {}

def test_line_as_None():
    assert parse_config(None) == {}

def test_line_with_duplicates():
    line3 = ["timeout=30", "retries=5", "malformed_line", "  mode = auto  ", "timeout=30"]
    assert parse_config(line3) == {'timeout': ['30', '30'], 'retries': '5', 'malformed_line': 'INVALID', 'mode': 'auto'}

def test_line_with_only_timeout():
    line5 = ["timeout=30"]
    assert parse_config(line5) == {'timeout': '30'}

def test_valid_line():
    line = ["timeout=30", "retries=5", "malformed_line", "  mode = auto  ", "timeout=60"]
    assert parse_config(line) == {'timeout': ['30', '60'], 'retries': ['5'], 'malformed_line': 'INVALID', 'mode': ['auto']}
