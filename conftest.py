import requests
import yaml
import pytest
import random
import string

with open('config.yaml') as f:
    data = yaml.safe_load(f)



@pytest.fixture()
def token():
    result = requests.post(url=data['login_site'],
                           data={"username": data['name'],
                                 "password": data['passwd']})
    t = result.json()["token"]
    return t


@pytest.fixture()
def text_title():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return text

@pytest.fixture()
def text_description():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    return text

@pytest.fixture()
def text_content():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
    return text

