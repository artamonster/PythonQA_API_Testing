import pytest
import cerberus
import requests
from http import HTTPStatus


class TestApi:

    def test_check_breweries_json_schema(self, endpoint, schema):
        response = requests.get(endpoint["list_breweries"])
        assert response.status_code == HTTPStatus.OK

        breweries_list = response.json()
        v = cerberus.Validator(schema["breweries_schema"])
        for brewery in breweries_list:
            assert v.validate(brewery)

    @pytest.mark.parametrize("id", [id for id in range(8040, 8042)])
    def test_get_breweries_valid_url_website(self, endpoint, id):
        response = requests.get(endpoint["get_breweries"].format(id))
        brewery_url = response.json()["website_url"]
        print(brewery_url)

    def test_search_breweries(self, endpoint, search_query):
        search_word, quantity = search_query[0], search_query[1]
        response = requests.get(endpoint["search_breweries"].format(search_word))
        assert len(response.json()) == quantity

    def test_autocomplete_search(self, endpoint, autocomplete_search_query):
        search_word, quantity = autocomplete_search_query[0], autocomplete_search_query[1]
        response = requests.get(endpoint["autocomplete_search_breweries"].format(search_word))
        assert len(response.json()) == quantity

    def test_not_existed_endpoint(self, endpoint):
        response = requests.get(endpoint["host"] + "/not_existed_url")
        assert response.status_code == HTTPStatus.NOT_FOUND
