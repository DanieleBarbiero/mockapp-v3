from mockapp.main import greet


def test_greet_returns_expected_text():
    assert greet() == "hello from mockapp"