import pytest

from run import app


def test_app_all_posts_status_code():
    respone = app.test_client().get('/api/posts/', follow_redirects = True)
    assert respone.status_code == 200, "Статус запроса всех постов неверный"
    assert respone.mimetype == 'application/json', 'Получен не json'
    

def test_app_all_posts_type_content():
    respone = app.test_client().get('/api/posts/', follow_redirects=True)
    assert type(respone.json) == list, "Получен не список"
    
    
def test_get_all_post_has_keys():
    keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    respone = app.test_client().get('/api/posts/', follow_redirects=True)
    first_keys = set(respone.json[0].keys())
    assert keys == first_keys, 'нужные ключи отсутствуют'
    
    
def test_app_one_posts_status_code():
    respone = app.test_client().get('/api/posts/1', follow_redirects = True)
    assert respone.status_code == 200, "Статус запроса всех постов неверный"
    assert respone.mimetype == 'application/json', 'Получен не json'
    
    
def test_app_one_posts_type_content():
    respone = app.test_client().get('/api/posts/1', follow_redirects=True)
    print (respone)
    assert type(respone.json) == dict, "Получен не словарь"
    

def test_get__post_has_keys():
    keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    respone = app.test_client().get('/api/posts/1', follow_redirects=True)
    first_keys = set(respone.json.keys())
    assert keys == first_keys, 'нужные ключи отсутствуют'