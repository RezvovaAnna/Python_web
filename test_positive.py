import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)



def test_create_post(token, text_title, text_description, text_content):
    # Проверка создания поста
    requests.post(url=data['post_site'], headers={"X-Auth-Token": token},
                 params={"title": text_title, "description": text_description,
                         "content": text_content})
    res_get = requests.get(url=data['post_site'], headers={"X-Auth-Token": token},
                           params={"owner": 'Me'})
    description_list = [i['description'] for i in res_get.json()['data']]
    assert text_description in description_list


def test_find_post(token, text_title):
    # Проверка наличия определенного загловка и отсутвия созданого пользователем поста в не его постах
    res_get = requests.get(url=data['post_site'],
                           headers={"X-Auth-Token": token},
                           params={"owner": "notMe"})
    title_list = [i['title'] for i in res_get.json()['data']]
    assert 'Cats' in title_list and text_title not in title_list


