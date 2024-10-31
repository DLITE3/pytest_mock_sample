import requests

class Request:
    def __init__(self, url: str):
        self.url = url
        self.response: object = None
        try:
            self.response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            print(e)
            self.response = requests.models.Response()
            self.response.status_code = 404
    
    def get_data(self) -> requests.models.Response:
        return self.response