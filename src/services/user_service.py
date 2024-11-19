from repo.user_repo import UserRepository


class UserService:
    def __init__(self, db_config):
        self.user_repository = UserRepository(db_config)

    def register_user(self, username: str, email: str, password: str):
        # Business logic for registering a user, e.g., checking if email already exists
        existing_user_username = self.user_repository.get_user_by_username(
            username=username)
        if existing_user_username:
            return {"error": "User with this username already exists."}
        existing_user_email = self.user_repository.get_user_by_email(
            email=email)
        if existing_user_email:
            return {"error": "User with this email already exists."}
        user_id = self.user_repository.create_user(username, email, password)
        if user_id:
            return {"message": "User registered successfully.", "user_id": user_id}
        else:
            return {"error": "User registration failed."}

    def get_user(self, user_id: int):
        # Business logic for getting a user by ID
        user = self.user_repository.get_user_by_id(user_id)
        if user:
            return user
        else:
            return {"error": "User not found."}

    def update_user_info(self, user_id: int, username: str = None, email: str = None, password: str = None, streak: int = None):
        # Business logic for updating user information
        updated = self.user_repository.update_user(
            user_id, username, email, password, streak)
        if updated:
            return {"message": "User information updated successfully."}
        else:
            return {"error": "Failed to update user information."}

    def delete_user(self, user_id: int):
        # Business logic for deleting a user
        deleted = self.user_repository.delete_user(user_id)
        if deleted:
            return {"message": "User deleted successfully."}
        else:
            return {"error": "Failed to delete user."}
