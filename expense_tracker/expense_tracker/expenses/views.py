from django.shortcuts import render, redirect
from expense_tracker.expenses.forms import ExpenseForm
from expense_tracker.expenses.models import Expense
from expense_tracker.profiles.models import Profile


def home_page(request):
    profile = Profile.objects.first()

    if not profile:
        return redirect('create profile')

    expenses = Expense.objects.all()

    context = {
        'expenses': expenses,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ExpenseForm()

    context = {'form': form}
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ExpenseForm(instance=expense)

    context = {'form': form}
    return render(request, 'expense-edit.html', context)


def delete_expense(request):
    pass