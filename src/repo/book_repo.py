from models.book import BookModel
from datetime import date


class BookRepository:
    def __init__(self, db_config):
        self.book_model = BookModel(db_config)

    def create_book(self, title: str,
                    author: str,
                    publication_date: date,
                    release_date: date,
                    rating: float = 0):
        return self.book_model.create_book(title, author, publication_date, release_date, rating)

    def get_book_by_id(self, book_id: int):
        return self.book_model.get_book_by_id(book_id)

    def get_book_by_title(self, book_title: str):
        return self.book_model.get_book_by_title(book_title)

    def update_book(self, book_id: int, title: str = None,
                    author: str = None, publication_date: date = None,
                    rating: float = None, release_date: date = None):
        return self.book_model.update_book(book_id=book_id
                                           ,title=title
                                           ,author=author
                                           ,publication_date=publication_date
                                           ,rating=rating,release_date=release_date)
    
    def delete_book(self, book_id:int):
        return self.book_model.delete_book(book_id)