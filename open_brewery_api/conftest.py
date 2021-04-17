import pytest

HOST = "https://api.openbrewerydb.org/"


@pytest.fixture(scope="session")
def endpoint():
    endpoint_dict = {
        "host": HOST,
        "list_breweries": HOST + "breweries",
        "get_breweries": HOST + "breweries/{}",
        "search_breweries": HOST + "breweries/search?query={}",
        "autocomplete_search_breweries": HOST + "breweries/autocomplete?query={}"}
    return endpoint_dict


@pytest.fixture(scope="session")
def schema():
    schemas = {"breweries_schema": {"id": {"type": "integer"},
                                    "obdb_id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "brewery_type": {"type": "string"},
                                    "street": {"type": "string", 'nullable': True},
                                    "address_2": {"type": "string", 'nullable': True},
                                    "address_3": {"type": "string", 'nullable': True},
                                    "city": {"type": "string"},
                                    "state": {"type": "string"},
                                    "county_province": {"type": "string", 'nullable': True},
                                    "postal_code": {"type": "string"},
                                    "country": {"type": "string"},
                                    "longitude": {"type": "string", 'nullable': True},
                                    "latitude": {"type": "string", 'nullable': True},
                                    "phone": {"type": "string", 'nullable': True},
                                    "website_url": {"type": "string", 'nullable': True},
                                    "updated_at": {"type": "string"},
                                    "created_at": {"type": "string"}},

               "autocomplete_schema": {"id": {"type": "integer"},
                                       "name": {"type": "string"}}

               }
    return schemas


@pytest.fixture(scope="session", params=[("beer", 419), ("cooper", 27), ("Мытищинский пивзавод", 0)])
def search_query(request):
    return request.param


@pytest.fixture(scope="session", params=[("beer", 15), ("cooper", 15), ("Мытищинский пивзавод", 0)])
def autocomplete_search_query(request):
    return request.param
