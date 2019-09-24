from django.shortcuts import render

# crawler
import requests
from bs4 import BeautifulSoup as bs


# Create your views here.

def index(request):
    return render(request , 'index.html')

def menu(request):
    
    
    # req = requests.get('https://dorm.pusan.ac.kr/mdorm/function/mealPlan/40000403')
    # html = req.text
    # soup = bs(html, 'html.parser')

    # divs = soup.find('div', {'class' : 'row no_margin_horizonals'})
    
    # for div in divs:
    #     menu_list = div.text


    return render(request, 'menu.html' , {'menu_lists':menu_list})