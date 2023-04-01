import requests
import pytest
import json
import jsonpath


def test_get_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'

    response = requests.get(base_url + endpoint)
    assert response.status_code == 200, "Status code doesn't match"


def test_post_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    request_json = {'id': 1,
                    'idBook': 1,
                    'firstName': 'Fredy',
                    'lastName': 'Mercury'}

    response = requests.post(base_url + endpoint, json=request_json)
    assert response.status_code == 200, "Status code doesn't match"
    print(request_json)


def test_put_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    authors_id = '1'
    request_json = {"id": 3,
                    'idBook': 3,
                    'firstName': 'Vard',
                    'lastName': 'Kar'
                    }

    response = requests.put(base_url + endpoint + authors_id, json=request_json)
    assert response.status_code == 200, "Status code doesn't match"
    print(request_json)


def test_delete_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    authors_id = '1'
    request_json = {"id": 1}

    response = requests.delete(base_url + endpoint + authors_id, json=request_json)
    assert response.status_code == 200, "Status code doesn't match"
    print(request_json)
