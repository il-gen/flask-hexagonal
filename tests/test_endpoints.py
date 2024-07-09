# domain/tests/test_flask_adapter.py
from flask import url_for
import pytest
from unittest import mock
from flask.testing import FlaskClient
from project import create_app
from project.domain.book_service import BookService
from project.domain.entities import Book
from project.adapters.assembly import Container

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    
    yield app
    # clean up / reset resources here

@pytest.fixture()
def client(app) -> FlaskClient:
    """Fixture to create a test client for the Flask app."""
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_get_all_books(client: FlaskClient):
    """Test GET /books endpoint."""
    response = client.get('/books')
    assert response.status_code == 200

    books = response.json
    assert isinstance(books, list)
    assert len(books) > 0
    assert all(isinstance(book['title'], str) for book in books)

def test_get_book(app, client: FlaskClient):
    """Test GET /books/<book_id> endpoint."""
    # Assuming book with ID 1 exists
    mock_book_id=1
    mock_title="Javascript Programming"
    mock_author="Micheella Doremi"
    book_service_mock = mock.Mock(spec=BookService)
    book_service_mock.get_book.return_value= Book(
        book_id=mock_book_id, 
        title=mock_title, 
        author=mock_author
    )

    with app.container.book_service.override(book_service_mock):
        response = client.get(f'/books/{mock_book_id}')

    assert response.status_code == 200

    book = response.json
    assert isinstance(book, dict)
    assert 'title' in book
    assert isinstance(book['title'], str)
    assert 'author' in book
    assert isinstance(book['author'], str)

    assert book['book_id'] == mock_book_id
    assert book['author'] == mock_author
    assert book['title'] == mock_title
    
def test_get_nonexistent_book(client: FlaskClient):
    """Test GET /books/<nonexistent_book_id> endpoint."""
    nonexistent_book_id = 999

    response = client.get(f'/books/{nonexistent_book_id}')
    assert response.status_code == 404

    error_message = response.data.decode('utf-8')
    assert 'Book with id 999 not found' in error_message

