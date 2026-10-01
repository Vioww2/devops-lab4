from hello import get_message


def test_get_message():
    assert get_message() == "Hello from Vioww2"


def test_get_message_is_not_empty():
    assert get_message().strip()
