from models.user import UserModel
from pydantic import EmailStr


class UserRepository:
    def __init__(self, db_config):
        self.user_model = UserModel(db_config)

    def create_user(self, username: str, email: str, password: str):
        return self.user_model.create_user(username, email, password)

    def get_user_by_id(self, user_id: int):
        return self.user_model.get_user_by_id(user_id)

    def update_user(self, user_id: int, username: str = None, email: str = None, password: str = None, streak: int = None):
        return self.user_model.update_user(user_id, username, email, password, streak)

    def delete_user(self, user_id: int):
        return self.user_model.delete_user(user_id)

    def get_user_by_email(self, email: EmailStr):
        return self.user_model.get_user_by_email(email)

    def get_user_by_username(self, username: str):
        return self.user_model.get_user_by_username(username=username)
