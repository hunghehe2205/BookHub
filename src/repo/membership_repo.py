from models.membership import MembershipModel
from datetime import date


class MembershipRepository:
    def __init__(self, db_config):
        self.membership_model = MembershipModel(db_config)

    def create_membership(self, user_id: int, type: str, expired_day: date, remaining_books: int):
        return self.membership_model.create_membership(user_id, type, expired_day, remaining_books)

    def get_membership_by_id(self, user_id: int):
        return self.membership_model.get_membership_by_user_id(user_id)

    def update_membership(self, user_id: int, type: str = None, expired_day: date = None, remaining_books: int = None):
        return self.membership_model.update_membership(user_id, type=type, expired_day=expired_day, remaining_books=remaining_books)

    def delete_membership(self, user_id: int):
        return self.membership_model.delete_membership(user_id)
