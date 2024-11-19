from repo.membership_repo import MembershipRepository
from datetime import date


class MembershipService:
    def __init__(self, db_config):
        self.membership_repository = MembershipRepository(db_config)

    def create_membership(self, user_id: int, type: str, expired_day: date, remaining_books: int):
        member_exist = self.membership_repository.get_membership_by_id(user_id)
        if member_exist:
            return {"error": "Membership with this UserID already exists."}
        membership_user_id = self.membership_repository.create_membership(
            user_id, type, expired_day, remaining_books)
        print(membership_user_id)
        if membership_user_id:
            return {"message": "Membership created successfully.", "membership_user_id": membership_user_id}
        else:
            return {"error": "Membership created failed."}

    def get_membership(self, user_id: int):
        membership = self.membership_repository.get_membership_by_id(user_id)

        if membership:
            return membership
        else:
            return {"error": "Membership not found."}

    def update_membership_info(self, user_id: int, type: str = None, expired_day: date = None, remaining_books: int = None):
        # Business logic for updating user information
        updated = self.membership_repository.update_membership(
            user_id, type=type, expired_day=expired_day, remaining_books=remaining_books)
        if updated:
            return {"message": "Membership updated successfully."}
        else:
            return {"error": "Failed to update membership information."}

    def delete_membership(self, user_id: int):
        # Business logic for deleting a user
        deleted = self.membership_repository.delete_membership(user_id=user_id)
        if deleted:
            return {"message": "Membership deleted successfully."}
        else:
            return {"error": "Failed to delete membership."}
