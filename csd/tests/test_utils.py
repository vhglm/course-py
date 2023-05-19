from gww.utils import create_url


def test_create_url():
    url = create_url("https://test.com", "collection", "method")
    assert url == "https://test.com/collection/method"
