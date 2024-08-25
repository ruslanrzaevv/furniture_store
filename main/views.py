from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'Главная - страница',
        'content': 'Магазин мебели Home ',

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас', 
        'text_on_page': 'Текст о том как наш магазин такой классный, и какой хороший товар'
    }
    return render(request, 'main/about.html', context)

