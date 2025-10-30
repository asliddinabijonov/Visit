from django.shortcuts import render
from django.views import View


class HomeViews(View):
    def get(self, request):
        carousel_items = [
            {
                'img': 'img/carousel-1.jpg',
                'small_title': 'Toshkent',
                'big_title': "Let's The World Together!",
                'text': "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
            },
            {
                'img': 'img/carousel-2.jpg',
                'small_title': 'Farg\'ona',
                'big_title': "Adventure Awaits!",
                'text': "Some other dummy text for the second slide."
            },
            {
                'img': 'img/carousel-3.jpg',
                'small_title': 'Samarqand  n ',
                'big_title': "Make Memories!",
                'text': "Another dummy text for the third slide."
            },
        ]

        context = {
            "carousel": carousel_items
        }
        return render(request, "index.html", context = context )