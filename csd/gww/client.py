from gww import reservoirs


class Client:
    def __init__(self, url="https://api.globalwaterwatch.earth"):
        self.url = url

    @property
    def reservoirs(self):
        return reservoirs.ReservoirCollection(self.url)
