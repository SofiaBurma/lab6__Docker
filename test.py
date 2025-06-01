import app

def test_hello():
    response = app.hello()
    assert response == "Hello Docker!"