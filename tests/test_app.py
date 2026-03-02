def test_root_redirect(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (301, 302, 307)
    assert response.headers.get("location") == expected_location


def test_get_activities_returns_expected_structure(client):
    # Arrange: nothing to prepare beyond fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    # known activity present
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
