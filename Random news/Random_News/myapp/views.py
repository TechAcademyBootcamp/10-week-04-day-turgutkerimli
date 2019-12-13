from django.shortcuts import render
import requests
import random

URL = requests.get('https://newsapi.org/v2/everything?q=bitcoin&from=2019-11-13&sortBy=publishedAt&apiKey=3f589812a9e1449dbef588464c4d90f4')
news =URL.json()
my_list = news["articles"]
rand_number = random.randrange(len(my_list))

print(my_list[rand_number]['author'])

# Create your views here.
def home_function(request):
    URL = requests.get('https://newsapi.org/v2/everything?q=bitcoin&from=2019-11-13&sortBy=publishedAt&apiKey=3f589812a9e1449dbef588464c4d90f4')
    news =URL.json()
    my_list = news["articles"]
    rand_number = random.randrange(len(my_list))
    context = {
        'image': my_list[rand_number]['urlToImage'],
        'title': my_list[rand_number]['title'],
        'description': my_list[rand_number]['description'],
        'date': my_list[rand_number]['publishedAt'],
        'author': my_list[rand_number]['author'],
    }
        
    return render(request, 'news.html', context)

