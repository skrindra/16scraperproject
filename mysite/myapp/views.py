from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.db import connection
# Create your views here.

def scrape(request):

    if request.method == "GET" and request.GET.get('delete'):
        Link.objects.all().delete()

    if request.method == "POST":
        site = request.POST.get('url', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            name = link.string  # get name of the link
            address = link.get('href')   # get address of the link
            # store in database
            Link.objects.create(name=name, address=address)
        return redirect('/')

    else:
        # retrieve data from db & display
        link_objects = Link.objects.all()
    return render(request, 'myapp/result.html', {'link_objects': link_objects})



# # view to delete data from db
# def clear(request):
        
#     Link.objects.all().delete()
#     return render(request, 'myapp/result.html')
