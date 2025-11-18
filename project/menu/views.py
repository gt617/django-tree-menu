from django.shortcuts import render


def tree(request):
    return render(request, "base.html")
