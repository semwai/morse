import pytest
from starlette.testclient import TestClient # noqa

from app import app
from alphabets import table
from morse import encode, decode


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


def test_encode():
    assert encode("SOS", table('en')) == '... --- ...'


def test_decode():
    assert decode("... --- ...", table('en')) == 'SOS'


def test_decode_exception():
    with pytest.raises(NotImplementedError):
        decode("... --- ...", table('es'))


def test_encode_api(test_app):
    response = test_app.get("/encode?text=SOS")
    assert response.status_code == 200
    assert response.json() == {"data": "... --- ..."}


def test_decode_api(test_app):
    response = test_app.get("/decode?text=... --- ...")
    assert response.status_code == 200
    assert response.json() == {"data": "SOS"}


def test_decode_api_exception(test_app):
    response = test_app.get("/decode?text=... --- ...&lang=es")
    assert response.status_code == 400

