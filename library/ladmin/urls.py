from django.urls import path
from ladmin.views import *

urlpatterns = [
    path('', ahome, name='ahome'),
    
    path('books/', admin_books, name='admin_books'),
    path('books/add/', admin_add_book, name='admin_add_book'),
    path('categories/', admin_categories, name='admin_categories'),
    path('categories/add/', admin_add_category, name='admin_add_category'),
    path('custuser/', custuser, name='acustuser'),
    
   
    path('borrowings/', admin_borrowings, name='admin_borrowings'),
    path('borrowings/add/', admin_add_borrowing, name='admin_add_borrowing'),
    path('borrowings/edit/<int:borrowing_id>/', admin_edit_borrowing, name='admin_edit_borrowing'),
    
    path('add_purchase/', admin_add_purchase, name='admin_add_purchase'),
    path('purchases/', admin_purchases, name='admin_purchases'),
    
    


]

