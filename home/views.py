from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')