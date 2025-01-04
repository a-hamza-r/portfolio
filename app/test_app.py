import pytest

from run import app as application


@pytest.fixture()
def app():
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture
def client(app):   
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_api(client):
    response = client.get("/")
    assert response.status_code == 200

    response = client.get("/experience/")
    assert response.status_code == 200

    response = client.get("/cv/")
    assert response.status_code == 200

    response = client.get("/contact/")
    assert response.status_code == 200

    response = client.get("/projects/")
    assert response.status_code == 200

    response = client.get("/publications/")
    assert response.status_code == 200

    response = client.get("/projects/research-equiv-check/")
    assert response.status_code == 200

    response = client.get("/projects/dev-test-ml-compiler/")
    assert response.status_code == 200
