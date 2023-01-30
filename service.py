import api_call
from concurrent.futures import ThreadPoolExecutor
from faker import Faker
import configparser
import random

fake = Faker()

def parse_config(config_path: str) -> dict:
    config = configparser.ConfigParser()
    config.read(config_path)

    config_dict = {}
    for section in config.sections():
        for option in config.options(section):
            config_dict[option] = config.get(section, option)

    return config_dict


def run_bot(config_path: str):
    config = parse_config(config_path)
    
    config['REGISTER_URL'] = config['base_uri'] + '/register'
    config['LOGIN_URL'] = config['base_uri'] + '/login'
    config['POST_URL'] = config['base_uri'] + '/post'
    config['POSTS_URL'] = config['base_uri'] + '/posts'

    users_data = prepare_users_data(int(config['number_of_users']))

    with ThreadPoolExecutor() as executor:
        results = [executor.submit(api_call.register_users, config['REGISTER_URL'], **user) for user in users_data]

    login_users = [{k: v for k, v in user.items() if k != 'name'} for user in users_data]
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(api_call.login_users, config['LOGIN_URL'], **user) for user in login_users]
    for result in results:
        for user in login_users:
            if user['email'] == result._result['email']:
                user['jwt'] = result._result['jwt']

    posts = prepare_data_for_posts(int(config['max_posts_per_user']), login_users)
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(api_call.create_posts, config['POST_URL'], **post) for post in posts]
    posts_info = api_call.get_all_posts(config['POSTS_URL'], login_users[0]['jwt'])
    likes_data = prepare_likes_data(int(config['max_likes_per_user']), login_users, posts_info, config['base_uri'])
    with ThreadPoolExecutor() as executor:
        results = [executor.submit(api_call.like_posts, **like_data) for like_data in likes_data]


def prepare_likes_data(max_num_of_likes: int, logined_users: list[dict], posts_data: list[dict], base_uri: str) -> list[dict]:
    num_of_likes = random.randint(1, max_num_of_likes)
    num_of_likes = num_of_likes if num_of_likes < len(posts_data) else len(posts_data)
    likes = []
    for user in logined_users:
        for i in range(num_of_likes):
            likes.append({
                'url': f"{base_uri}/posts/{posts_data[i]['id']}/action/like",
                'bearer_token': user['jwt']
            })
    return likes


def prepare_data_for_posts(max_num_of_posts: int, logined_users: dict) -> list[dict]:
    num_of_posts = random.randint(1, max_num_of_posts)
    posts = []
    for user in logined_users:
        for i in range(num_of_posts):
            posts.append(
                {
                    'bearer_token': user['jwt'],
                    'content': fake.word()
                }
            )
    return posts


def prepare_users_data(num_of_users: int) -> list[dict]:
    users_data = []

    for i in range(num_of_users):
        users_data.append(
            {
                'name': fake.name(),
                'email': fake.email(),
                'password': fake.password()
            }
        )
    return users_data
