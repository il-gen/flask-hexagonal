# domain/tests/test_services.py
import pytest
from dependency_injector import providers, containers
from project.domain.book_service import BookServiceImpl, BookNotFoundException
from project.adapters.db_repo import InMemoryBookRepository

@pytest.fixture(scope='function')
def container():
    # Define a container for testing purposes
    class TestContainer(containers.DeclarativeContainer):
        book_service = providers.Singleton(
            BookServiceImpl, 
            book_repository=InMemoryBookRepository()
        )

    # Create an instance of the container
    return TestContainer()

def test_get_existing_book(container):
    book_service = container.book_service()
    book_id = 1
    expected_title = "Python Programming"
    
    book = book_service.get_book(book_id)
    
    assert book.title == expected_title

def test_get_nonexistent_book(container):
    book_service = container.book_service()
    book_id = 999
    
    with pytest.raises(BookNotFoundException):
        book_service.get_book(book_id)

def test_get_all_books(container):
    book_service = container.book_service()
    expected_titles = ["Python Programming", "Flask Web Development"]
    
    books = book_service.get_all_books()
    
    assert len(books) == len(expected_titles)
    for book in books:
        assert book.title in expected_titles
