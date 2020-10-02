import requests



def signup():
    url = BASE_URL + "users/"
    payload = {
        'username': 'testUser3', 
        'password': 'P@ssw0rd1234', 
        'email': 'email@mail.com'
        }
    r = requests.post(url, data=payload)
    if r.status_code == 201:
        print("Successfully signed up")
    else:
        print("Failed to sign up")


def get_token():
    url = BASE_URL + "jwt/create/"
    payload = {
        'username': 'testUser', 
        'password': 'P@ssw0rd1234', 
        }
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        token = r.json()["access"]
        print("Successfully obtained token")
        return token
    else:
        Print("Failed to obtain token")
        return None


def get_user_info(token):
    url = BASE_URL + "users/me/"
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print("used token to access user info")



signup()
token = get_token()
get_user_info(token)