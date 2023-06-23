from ninja import NinjaAPI

#BOOKS
from books.api import router as books_router
from user.api import router as user_router
from user.api import router as loan_router

api = NinjaAPI()

#BOOK ROUTE
api.add_router('books/', books_router)
#USER ROUTE
api.add_router('user/', user_router)
#LOAN ROUTE
api.add_router('loan/', loan_router)