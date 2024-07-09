from abc import ABC, abstractmethod
from .entities import Book
from project.domain.db_port import BookRepository

class BookNotFoundException(Exception):
    pass

class BookService(ABC):
    @abstractmethod
    def get_book(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def get_all_books(self) -> list:
        pass

class BookServiceImpl(BookService):
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def get_book(self, book_id: int) -> Book:
        book = self.book_repository.find_by_id(book_id)
        if not book:
            raise BookNotFoundException(f"Book with id {book_id} not found")
        return book

    def get_all_books(self) -> list:
        return self.book_repository.find_all()