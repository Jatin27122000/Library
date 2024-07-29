from django.urls import path
from cust.views import home,logins,register,logouts,user_borrowings,profile,editpro

urlpatterns = [
    path('',home,name='home'),
    path('login/',logins,name='login'),
    path('register/',register,name='register'),
    path('logout/',logouts,name='logout'),
    path('borrowings/', user_borrowings, name='user_borrowings'),
    path('profilepage/',profile,name='profilepage'),
    path('edit_profile/<int:id>/', editpro, name='edit_profile'),
]
