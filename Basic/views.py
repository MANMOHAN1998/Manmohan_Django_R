from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Detail
from .serializer import DetailSerializer
import requests
##
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
##

#creating my first REST API here
@api_view(['GET','POST'])
def GetDetail(request):
    name = Detail.objects.all()
    serializer = DetailSerializer(name, many=True)
    return Response(serializer.data)

# Create your views here.
def index(request):
    varables = {
        "temp_no" : 1
    }
    return render(request, 'index.html', varables)
    # return HttpResponse('This is the start')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is the About')

def know(request):
    response = requests.get('http://127.0.0.1:8000/post/')
    data = response.json()
    return render(request, 'know.html', {'data': data})

def contact(request):
    return render(request, 'contact.html')


def find_item(request):
    x = request.POST['myvalue']
    y = request.POST['page_no']
    # link = list()
    # for a in range(10):
    #     a+=1
    link = 'https://'+'www.flipkart.com/search?q='+str(x)+'&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    if y == '':
        pass
    else:
        link = link + '%3D2&page='+str(y)
        # link.append(x)
# print(link)
    link = link
    products = [] #list to store name of the product
    prices = [] #list to store price of the product
    ratings = [] #list to store rating of the product
    url_of_product = [] #list to store rating of the product

    # #insert the wesite url that will be scraped
    # for a in link:
    req = requests.get(link)

    soup = BeautifulSoup(req.content, "html.parser")
    # data = soup.prettify()

    # #find the data and append data in respective list
    name = soup.find_all("div", attrs={'class': '_4rR01T'})
    for row in name:
        a = row.text
        products.append(a)
    price = soup.find_all("div", attrs={'class': '_30jeq3 _1_WHN1'})
    for row in price:
        b = row.text
        prices.append(b)
    rating = soup.find_all("div", attrs={'class': 'gUuXy-'})
    for A in rating:
        print(A)
    for row in rating:
        c = row.text
        R = re.findall('([1-9].[1-9])', c)
        ratings.append(R[0])
    for d in soup.find_all("a", attrs={'class': '_1fQZEK'}, href=True):
        d = 'https://www.flipkart.com' + d['href']
        url_of_product.append(d)
    data = {'link':link,
            'products':len(products),
            'prices':len(prices),
            'ratings':len(ratings),
            'url_of_product':len(url_of_product)}
    # data = ratings

    #output the data form of a csv file
    output_column_name = {'Title':products,'Price':prices,'URL of Item':url_of_product}
    output = pd.DataFrame(output_column_name)
    data = output.to_html
    # output.to_csv('flipcart_scrapping.csv')
        
    return render(request, 'Item.html', {'link':link,'data':data})