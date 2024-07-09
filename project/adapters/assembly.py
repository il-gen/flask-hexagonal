from dependency_injector import containers, providers
from project.domain.book_service import BookServiceImpl
from project.adapters.db_repo import InMemoryBookRepository
from dependency_injector import containers, providers
from flask import Flask
# Dependency Injection configuration
class Container(containers.DeclarativeContainer):
    
    app = providers.Dependency(instance_of=Flask)

    wiring_config = containers.WiringConfiguration(packages=["project.blueprints"])
    
    book_repository = providers.Factory(
                    InMemoryBookRepository
                )

    book_service =  providers.Factory( 
                        BookServiceImpl, 
                        book_repository= book_repository
                    )


