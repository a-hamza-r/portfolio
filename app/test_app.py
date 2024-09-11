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

    response = client.get("/experience.html")
    assert response.status_code == 200

    response = client.get("/cv.html")
    assert response.status_code == 200

    response = client.get("/contact.html")
    assert response.status_code == 200

    response = client.get("/projects.html")
    assert response.status_code == 200

    response = client.get("/publications.html")
    assert response.status_code == 200

