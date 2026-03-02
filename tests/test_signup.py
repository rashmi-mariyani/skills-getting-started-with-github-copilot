def test_signup_and_unregister_flow(client):
    # Arrange
    activity = "Chess Club"
    email = "testuser@example.com"

    # Precondition: email not already signed up
    participants = client.get("/activities").json()[activity]["participants"]
    assert email not in participants

    # Act: sign up
    signup_resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert: signup succeeded and participant is present
    assert signup_resp.status_code == 200
    participants_after = client.get("/activities").json()[activity]["participants"]
    assert email in participants_after

    # Act: unregister
    unregister_resp = client.delete(f"/activities/{activity}/unregister", params={"email": email})

    # Assert: unregister succeeded and participant removed
    assert unregister_resp.status_code == 200
    participants_final = client.get("/activities").json()[activity]["participants"]
    assert email not in participants_final


def test_signup_existing_returns_400(client):
    # Arrange
    activity = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing_email})

    # Assert
    assert resp.status_code == 400


def test_unregister_nonexistent_returns_404(client):
    # Arrange
    activity = "Chess Club"
    unknown = "unknown@example.com"

    # Act
    resp = client.delete(f"/activities/{activity}/unregister", params={"email": unknown})

    # Assert
    assert resp.status_code == 404
