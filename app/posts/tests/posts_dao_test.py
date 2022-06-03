import os

import pytest

from app.posts.dao.posts_dao import PostsDAO


class TestPostsDao:
    @pytest.fixture
    def posts_dao(self):
        # print(os.getcwd())
        return PostsDAO("../../../data/posts.json")
    
    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    
    def test_get_all_chek_type(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, "ошибка в типе всех постов"
        assert type(posts[0]) == dict, "ошибка в типе одного поста"
    
    def test_get_all_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())
        assert first_post_keys == keys_expected, 'полученные данные неверны'
    
    def test_get_one_chek_type(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert type(post) == dict, "ошибка в типе одного поста"
    
    def test_get_one_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys_expected, 'полученные данные неверны'
    
    parametrs_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]
    
    #данные для тестирования search
    queries_and_responses = [("еда", [1]), ("дом", [2, 7, 8]), ("Дом", [2, 7, 8]), ("а", [1, 2, 3, 4, 5, 6, 7, 8])]
    
    @pytest.mark.parametrize("post_pk", parametrs_to_get_by_pk)
    def test_get_one_chek_type_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_by_pk(post_pk)
        assert post["pk"] == post_pk, "Номер запрошенного поста не соответствует не соответствует номеру полученного"
    
    """тестирование результатов поиска"""
    
    def test_search_line(self, posts_dao):
        posts = posts_dao.search("а")
        assert type(posts) == list, "Результат поиска должен быть списком"
        assert type(posts[0]) == dict, "Результат поиска должен быть словарем"
        
    @pytest.mark.parametrize("query, post_pks", queries_and_responses)
    def test_search_correct_match(self, posts_dao, query, post_pks):
        posts = posts_dao.search(query)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == post_pks, f'Неверный поиск по запросу {query}'
    
    def test_search_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.search("а")[0]
        post_keys = set(post.keys())
        assert post_keys == keys_expected, 'полученные ключи неверны'

    """Тестирование по пользователю"""
    
    def test_get_by_user_chek_type(self, posts_dao):
        posts = posts_dao.get_by_user("leo")
        assert type(posts) == list, "Результат поиска должен быть списком"
        assert type(posts[0]) == dict, "Результат поиска должен быть словарем"
        
    def test_get_by_user_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_by_user("leo")[0]
        post_keys = set(post.keys())
        assert post_keys == keys_expected, 'полученные ключи неверны'
        
    parametrs_to_get_by_user = [('leo', [1, 5]), ('hank', [3, 7]), ('Иван Иванов', [])]
    
    @pytest.mark.parametrize('user_name, correct_pks', parametrs_to_get_by_user)
    def test_get_by_user_correct_match(self, posts_dao, user_name, correct_pks):
        posts = posts_dao.get_by_user(user_name)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == correct_pks, f'Неверный поиск по пользователю {user_name}'