from abc import ABC, abstractmethod
from project.domain.entities import Book

class BookRepository(ABC):
    @abstractmethod
    def find_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass
