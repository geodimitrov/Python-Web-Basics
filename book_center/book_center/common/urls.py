from django.urls import path
from book_center.common.views import homepage_view


urlpatterns = [
    path('', homepage_view, name='home page')
]