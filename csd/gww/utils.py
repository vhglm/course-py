import requests


def create_url(base_url, *parts):
    return "/".join([base_url, *parts])

def send_request(url, *args, **kwargs):
    return requests.get(url, *args, **kwargs).json()