from repo.book_repo import BookRepository
from datetime import date


class BookService:
    def __init__(self, db_config):
        self.book_repository = BookRepository(db_config)

    def add_book(self, title: str, author: str, publication_date: str, release_date: str, rating: float = 0):
        book_exist = self.book_repository.get_book_by_title(title)
        if book_exist:
            return {"error": "Book with this title already exists."}
        book_id = self.book_repository.create_book(
            title, author, publication_date, release_date)
        if book_id:
            return {"message": "Book created successfully.", "book_id": book_id}
        else:
            return {"error": "Book creation failed."}

    def get_book(self, book_id: int):
        book = self.book_repository.get_book_by_id(book_id)
        if book:
            return book
        else:
            return {"error": "User not found."}

    def update_book_info(self, book_id: int, title: str = None,
                         author: str = None, publication_date: date = None,
                         rating: float = None, release_date: date = None
                         ):
        updated = self.book_repository.update_book(
            book_id=book_id, title=title, author=author, publication_date=publication_date
            , rating=rating, release_date=release_date)
        if updated:
            return {"message": "Book information updated successfully."}
        else:
            return {"error": "Failed to update user information"}

    def delete_book(self, book_id: int):
        deleted = self.book_repository.delete_book(book_id)
        if deleted:
            return {"message": "Book deleted successfully."}
        else:
            return {"error": "Failed to delete book."}
