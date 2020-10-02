import requests
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class TestUserAuth:

    BASE_URL = "http://localhost:8000/auth/"
    SUCCESS_CODES = [200, 201]

    def __init__(self, username, password, email):
        self.user_pass = {
            'username': username, 
            'password': password, 
        }
        self.email = email
        self.token = None
        self.signup_url = self.BASE_URL + "users/"
        self.get_token_url = self.BASE_URL + "jwt/create/"
        self.get_user_info_url = self.BASE_URL + "users/me/"

    def signup(self):
        email = {'email': self.email}
        payload = {**self.user_pass, **email}
        r = self.handle_request(self.signup_url, "POST", payload)
        if r.status_code in self.SUCCESS_CODES:
            self.log_message(logging.INFO, f"Successfully signed up {self.user_pass}")
        else:
            self.log_message(logging.WARN, f"Failed to sign up {self.user_pass}")

    def get_token(self):
        payload = self.user_pass
        r = self.handle_request(self.get_token_url, "POST", payload)
        if r.status_code in self.SUCCESS_CODES:
            token = r.json()["access"]
            self.token = token
            self.log_message(logging.INFO, f"Successfully obtained token for {self.user_pass}")
        else:
            self.log_message(logging.WARN, f"Failed to obtain token for {self.user_pass}")

    def get_user_info(self):
        if self.token == None: raise Exception("You do not have a token yet")
        headers = {'Authorization': 'Bearer ' + self.token} 
        r = self.handle_request(self.get_user_info_url, "GET", headers)
        if r.status_code in self.SUCCESS_CODES:
            self.log_message(logging.INFO, f"used token to access user info for {self.user_pass}")
        else:
            self.log_message(logging.WARN, f"unable to access resource using token for {self.user_pass}")

    def handle_request(self, url, method, extra):
        try:
            if method == "GET":
                return requests.get(url, headers=extra)
            elif method == "POST":
                return requests.post(url, data=extra)
        except:
            print("Request failed")

    def log_message(self, level, message):
        if level == 20: logging.info('%s', message)
        if level == 30: logging.warning('%s', message)

    def run(self):
        self.signup()
        self.get_token()
        self.get_user_info()


if __name__ == "__main__":
    test_user_base = "tu"
    num_users = 10

    for i in range(1, num_users):
        user = TestUserAuth(f"{test_user_base}{i}", "P@ssw0rd1234", f"{test_user_base}{i}@email.com")
        user.run()


