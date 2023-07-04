import pytest

from app import app
from utils import is_valid_currency

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_valid_currency():
    assert is_valid_currency('USD') == True
    assert is_valid_currency('US') == False
    assert is_valid_currency('usd') == False
    assert is_valid_currency('123') == False
