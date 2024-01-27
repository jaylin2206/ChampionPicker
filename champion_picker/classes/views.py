from django.shortcuts import render
from classes.models import Class

from champions.models import Champion
# Create your views here.


def index(request):
    classes = Class.objects.all()
    champions = Champion.classes.through.objects.select_related('champion', 'class').all().order_by('class', 'champion')
    context = {'classes': classes, 'champions': champions}

    return render(request, 'classes.html', context)
