from project.domain.db_port import BookRepository
from project.domain.entities import Book

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {
            1: Book(book_id=1, title="Python Programming", author="John Doe"),
            2: Book(book_id=2, title="Flask Web Development", author="Jane Smith")
        }
    
    def find_by_id(self, book_id: int) -> Book:
        return self.books.get(book_id)
    
    def find_all(self) -> list:
        return list(self.books.values())