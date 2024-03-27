from django.shortcuts import render

def home_screen_view(request):
    # Your view logic here, if any
    return render(request, "index.html", {})