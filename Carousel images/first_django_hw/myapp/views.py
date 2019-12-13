from django.shortcuts import render

# Create your views here.
def carousel_function(request):
    print(request.COOKIES)
    context = {
        'carousel_images': ['/static/images/1.jpg','/static/images/2.jpg','/static/images/3.jpg','/static/images/4.jpg','/static/images/5.jpg']
    }
    return render(request, 'carousel.html', context)