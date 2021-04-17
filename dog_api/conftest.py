import pytest


HOST = "https://dog.ceo/"


@pytest.fixture(scope="session")
def endpoint():
    endpoint_dict = {
        "host": HOST,
        "list_all_breeds": HOST + "api/breeds/list/all",
        "random_image": HOST + "api/breeds/image/random",
        "images_by_breed": HOST + "api/breed/{}/images",
        "sub_breed_by_breed": HOST + "api/breed/{}/list"}
    return endpoint_dict


@pytest.fixture(params={
    HOST + "api/breeds/list/all": {"message": {"type": "dict",
                                               "allow_unknown": True,
                                               "schema": {"dogs": {"type": "list", "schema": {"type": "string"}}},
                                               },
                                   "status": {"type": "string"}},
    HOST + "api/breeds/image/random": {"message": {"type": "string", "regex": "https://.+jpg"},
                                       "status": {"type": "string"}},
    HOST + "api/breed/doberman/images": {"message": {"type": "list", "schema": {"type": "string"}},
                                      "status": {"type": "string"}},
    HOST + "api/breed/doberman/list": {"message": {"type": "list", "schema": {"type": "string"}},
                                    "status": {"type": "string"}},
}.items(), scope="session")
def schema(request):
    return request.param
