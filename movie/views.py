from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
	searchTerm = request.GET.get('searchMovie')
	return render(request, 'home.html', {'searchTerm':searchTerm})
def about(request):
	return HttpResponse('<h1>Welcome to About Page</h1>')
