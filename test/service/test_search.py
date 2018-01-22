import pytest


@pytest.mark.integration
def test_search(client):
    response = client.get(
        '/se/v1/search?keyword=swagger&limit=1&sengine=baidu',
        content_type='application/json',
        follow_redirects=True)
    assert response, 'No response'
