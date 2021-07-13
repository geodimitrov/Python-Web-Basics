from django.urls import path
from book_center.users.views import register_user_view

urlpatterns = [
    path('', register_user_view, name="register user")
]