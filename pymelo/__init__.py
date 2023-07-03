import requests


class PomeloError(Exception):
    pass


class Check:
    def __init__(self, username):
        self.base_url = "https://api.lixqa.de/v3/discord/pomelo/{username}"
        url = self.base_url.format(username=username)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get("data", {}).get("check", {}).get("errors"):
                error_message = data.get("data", {}).get("check", {}).get("errors")[0].get("message")
                raise PomeloError(error_message)
            else:
                self.username = data.get("data", {}).get("username")
                self.status = data.get("data", {}).get("check", {}).get("status")
                self.attempt = data.get("data", {}).get("check", {}).get("attempt")
        else:
            raise PomeloError("Failed to make API request.")

    def username(self):
        return self.username

    def status(self):
        return self.status

    def attempt(self):
        return self.attempt
