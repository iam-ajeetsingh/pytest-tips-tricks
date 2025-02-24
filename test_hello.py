from hello import more_hello, more_goodbye


def test_more_hello():
    assert "Hiii..." == more_hello()


def test_more_goodbye():
    assert "bye..." == more_goodbye()
