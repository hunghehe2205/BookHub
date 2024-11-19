from fastapi import APIRouter, HTTPException, status, Depends
from services.book_service import BookService
from schemas.book_schema import BookCreate, BookResponse, BookUpdate

router = APIRouter()


def get_book_service():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '0329782205',
        'database': 'ebook'
    }
    return BookService(db_config)


@router.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, book_service: BookService = Depends(get_book_service)):
    result = book_service.add_book(
        book.title, book.author, book.publication_date, book.release_date, book.rating
    )
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return BookResponse(book_id=result["book_id"],
                        title=book.title,
                        author=book.author,
                        publication_date=book.publication_date,
                        rating=book.rating,
                        release_date=book.release_date)


@router.get("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def get_book(book_id: int, book_service: BookService = Depends(get_book_service)):
    book = book_service.get_book(book_id)
    if "error" in book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=book["error"])
    return BookResponse(
        book_id=book["BookID"],
        title=book["Title"],
        author=book["Author"],
        publication_date=book["PublicationDate"],
        rating=book["Rating"],
        release_date=book["ReleaseDate"]
    )


@router.put("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book(book_id: int, book_update: BookUpdate, book_service: BookService = Depends(get_book_service)):
    result = book_service.update_book_info(book_id, book_update.title, book_update.author,
                                           book_update.publication_date, book_update.rating, book_update.release_date)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    updated_book = book_service.get_book(book_id)
    if "error" in updated_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=updated_book["error"])
    return BookResponse(book_id=updated_book["BookID"],
                        title=updated_book["Title"],
                        author=updated_book["Author"],
                        publication_date=updated_book["PublicationDate"],
                        rating=updated_book["Rating"],
                        release_date=updated_book["ReleaseDate"])


@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, book_service: BookService = Depends(get_book_service)):
    result = book_service.delete_book(book_id)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
