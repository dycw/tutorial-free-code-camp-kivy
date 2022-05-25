from project import negate


def test_negate() -> None:
    assert negate(True) is False
