from ninja import NinjaAPI

#BOOKS
from books.api import router as books_router

api = NinjaAPI()

#BOOK ROUTE
api.add_router('books/', books_router)