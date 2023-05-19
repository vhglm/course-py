from gww.utils import create_url, send_request


class ReservoirCollection:
    path: str = "reservoir"

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, id: int):
        return send_request(create_url(self.base_url, self.path, str(id)))
