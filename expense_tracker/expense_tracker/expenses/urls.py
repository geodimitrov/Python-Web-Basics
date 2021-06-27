from django.urls import path
from expense_tracker.expenses.views import home_page, create_expense, edit_expense, delete_expense

urlpatterns = [
    path('', home_page, name='home'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
]