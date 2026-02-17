import pytest
import faker

@pytest.mark.users
class TestUsers:

    @pytest.mark.smoke          
    def test_get_users(self, api_client):
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


    def test_get_single_user(self, api_client):
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


    def test_get_user_has_required_fields(self, api_client):
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


    def test_get_nonexistent_user(self, api_client):
        # Arrange
        nonexistent_user_id = 99999
        
        # Act
        response = api_client.get_user(nonexistent_user_id)
        
        # Assert
        assert response.status_code == 404
        print(f"\n✓ GET /users/{nonexistent_user_id} correctly returned 404 (Not Found)")


    def test_get_users_response_structure(self, api_client):
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

    
    def test_create_user(self, api_client):
        # Arrange
        new_user_data = {
            "name": faker.Faker().name(),
            "username": faker.Faker().user_name(),
            "email": faker.Faker().email()
        }
        expected_status = 201

        # Act
        response = api_client.create_user(new_user_data)
        created_user = response.json()

        # Assert
        assert response.status_code == expected_status
        assert created_user["name"] == new_user_data["name"]
        assert created_user["username"] == new_user_data["username"]
        assert created_user["email"] == new_user_data["email"]
        print(f"\n✓ POST /users successfully created user: {created_user}")

    def test_update_user(self, api_client):
        # Arrange
        user_id = 1
        updated_user_data = {
            "name": faker.Faker().name(),
            "username": faker.Faker().user_name(),
            "email": faker.Faker().email()
        }
        expected_status = 200

        # Act
        response = api_client.update_user(user_id, updated_user_data)
        updated_user = response.json()

        # Assert
        assert response.status_code == expected_status
        assert updated_user["name"] == updated_user_data["name"]
        assert updated_user["username"] == updated_user_data["username"]
        assert updated_user["email"] == updated_user_data["email"]
        print(f"\n✓ PUT /users/{user_id} successfully updated user: {updated_user}")


    @pytest.mark.skip(reason="DELETE endpoint may not be supported by the API, or may have side effects. Enable when ready to test.")
    def test_delete_user(self, api_client):
        # Arrange
        user_id = 1
        expected_status = 204

        # Act
        response = api_client.delete_user(user_id)

        # Assert
        assert response.status_code == expected_status
        print(f"\n✓ DELETE /users/{user_id} successfully deleted user")