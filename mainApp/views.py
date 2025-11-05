from symtable import Class

from django.shortcuts import render
from django.views import View

from .models import *


class HomeViews(View):
    def get(self, request):
        regions = Region.objects.all()
        carousel_items = [
            {
                'img': r.image.url if r.image else '',
                'title': r.name,
                'name': r.title,
            }
            for r in regions
        ]

        context = {
            "carousel": carousel_items
        }
        return render(request, "index.html", context = context )

class AboutViews(View):
    def get(self, request):
        return render(request, 'about.html')