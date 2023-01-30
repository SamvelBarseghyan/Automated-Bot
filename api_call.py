import requests


def register_users(url: str, name: str, email: str, password: str):
    data = {
        "name": name,
        "email": email,
        "password": password
    }

    response = requests.post(url, data)
    if response.status_code != 200:
        raise Exception("Can't register users!")
    return response.json()


def login_users(url: str, email: str, password: str) -> dict:
    data = {
        "email": email,
        "password": password
    }

    response = requests.post(url, data)
    if response.status_code != 200:
        raise Exception("Can't login!")
    res = response.json()
    res['email'] = email

    return res

def create_posts(url: str, bearer_token: str, content: str) -> dict:
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    data = {
        "content": content
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Can't create post!")
    return response.json()


def get_all_posts(url: str, bearer_token: str) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Can't get data about posts!")
    return response.json()


def like_posts(url: str, bearer_token: str) -> dict:
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        raise Exception("Can't like post!")
    return response.json()