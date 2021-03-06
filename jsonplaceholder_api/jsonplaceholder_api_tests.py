import pytest
import cerberus
import requests
from http import HTTPStatus


class TestApi:

    def test_posts_check(self, endpoint):
        response = requests.get(endpoint["posts"].format(''))
        assert response.status_code == HTTPStatus.OK
        posts = response.json()
        assert len(posts) == 100

    def test_albums_check(self, endpoint):
        response = requests.get(endpoint["albums"].format(''))
        assert response.status_code == HTTPStatus.OK
        albums = response.json()
        assert len(albums) == 100

    @pytest.mark.parametrize("post_id,user_id", [(12, 2), (7, 1), (21, 3)])
    def test_posts_data_check(self, endpoint, post_id, user_id):
        response = requests.get(endpoint["posts"].format(post_id))
        assert response.json()["userId"] == user_id

    def test_endpoint_schemas(self, schema):
        url, schema = schema[0], schema[1]
        response = requests.get(url).json()
        v = cerberus.Validator(schema)
        assert v.validate(response)

    def test_not_existed_endpoint(self, endpoint):
        response = requests.get(endpoint["host"] + "/not_existed_url")
        assert response.status_code == HTTPStatus.NOT_FOUND
