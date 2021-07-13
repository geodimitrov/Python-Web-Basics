from django.urls import path
from book_center.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home page')
]