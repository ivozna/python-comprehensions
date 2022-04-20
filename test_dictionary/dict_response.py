import requests

class TestVerifyResponse:
    NAMES = ['blue', 'green']

    def get_response(self):
        r = requests.get('http://127.0.0.1:5000/bunny')
        return r.json()

    def verify_response(self, response):
        error = None
        for name in self.NAMES:
            if response[name] != 'iscolor':
                error = True 
        if error:
            return False
        return True

    def test_verify_response(self):
        response = self.get_response()
        assert self.verify_response(response) 
