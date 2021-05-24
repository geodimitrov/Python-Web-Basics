from django.shortcuts import render


def index(req):
    context = {"Name": "Georgi"}
    return render(req, "index.html", context)