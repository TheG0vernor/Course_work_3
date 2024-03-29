import json

from constants import DATA_POSTS, DATA_COMMENTS


class Basic:  # базовый класс
    def __init__(self, path_posts=DATA_POSTS, username=None, query=None, pk=None, path_comments=DATA_COMMENTS, post_id=None, len_comments=0):
        self.pk = pk
        self.query = query
        self.username = username
        self.path_posts = path_posts
        self.len_comments = len_comments
        self.post_id = post_id
        self.path_comments = path_comments

    def get_posts_all(self):
        """Возвращает список словарей с постами"""
        with open(self.path_posts, encoding='utf-8') as f:  # открыть файл с данными
            dictionary = json.load(f)
        return dictionary

    def get_comments_all(self):
        """Возвращает список словарей с комментариями"""
        with open(self.path_comments, encoding='utf-8') as f:  # открыть файл с данными
            dictionary = json.load(f)
        return dictionary
