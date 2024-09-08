from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152424',
        'name': 'Argya Farel Kasyara',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)