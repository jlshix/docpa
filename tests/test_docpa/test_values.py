"""docpa.values 的测试"""

from docpa.values import AnyValue


def test_any_value():
    raw = "any"
    av = AnyValue.parse(raw)
    assert av.value == raw
    assert av.dict() == {"type_name": "any", "value": raw}
