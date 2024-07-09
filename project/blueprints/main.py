from flask import Blueprint, jsonify
from project.adapters.assembly import Container
from project.domain.book_service import BookService, BookNotFoundException
from dependency_injector.wiring import inject, Provide

main = Blueprint('main', __name__)

@main.route('/books')
@inject
def get_all_books_route(book_service: BookService = Provide[Container.book_service]):
    books = book_service.get_all_books()
    return jsonify([book.to_dict() for book in books]), 200

@main.route('/books/<int:book_id>')
@inject
def get_book_route(book_id: int, book_service: BookService = Provide[Container.book_service]):
    try:
        book = book_service.get_book(book_id)
        return jsonify(book.to_dict()), 200
    except BookNotFoundException as e:
        return str(e), 404