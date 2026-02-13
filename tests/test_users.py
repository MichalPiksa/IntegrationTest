def test_get_users(api_client):
    # Arrange
    expected_status = 200
    
    # Act
    response = api_client.get_users()
    users = response.json()
    
    # Assert
    assert response.status_code == expected_status
    assert isinstance(users, list)
    assert len(users) > 0
    print(f"\n✓ GET /users returned {len(users)} users")
    print(f"  First user: {users[0]}")


def test_get_single_user(api_client):
    # Arrange
    user_id = 1
    expected_status = 200
    
    # Act
    response = api_client.get_user(user_id)
    user = response.json()
    
    # Assert
    assert response.status_code == expected_status
    assert user["id"] == user_id
    assert "username" in user
    assert "email" in user
    print(f"\n✓ GET /users/{user_id} returned user: {user}")


def test_get_user_has_required_fields(api_client):
    # Arrange
    user_id = 2
    required_fields = ["id", "name", "username", "email"]
    
    # Act
    response = api_client.get_user(user_id)
    user = response.json()
    
    # Assert
    assert response.status_code == 200
    for field in required_fields:
        assert field in user, f"Missing required field: {field}"
    print(f"\n✓ User ID {user_id} contains all required fields: {required_fields}")
    print(f"  User data: {user}")


def test_get_nonexistent_user(api_client):
    # Arrange
    nonexistent_user_id = 99999
    
    # Act
    response = api_client.get_user(nonexistent_user_id)
    
    # Assert
    assert response.status_code == 404
    print(f"\n✓ GET /users/{nonexistent_user_id} correctly returned 404 (Not Found)")


def test_get_users_response_structure(api_client):
    # Arrange
    expected_status = 200
    expected_fields_per_user = ["id", "name", "username", "email"]
    
    # Act
    response = api_client.get_users()
    users = response.json()
    
    # Assert
    assert response.status_code == expected_status
    assert all(isinstance(user, dict) for user in users)
    for user in users[:3]:
        for field in expected_fields_per_user:
            assert field in user, f"User missing field: {field}"
    
    print(f"\n✓ All users contain required fields: {expected_fields_per_user}")
    print(f"  Sample users (first 3):")
    for user in users[:3]:
        print(f"    - ID {user['id']}: {user['name']} ({user['username']}) - {user['email']}")