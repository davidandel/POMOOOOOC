from django.shortcuts import render, get_object_or_404
from .models import Recept

def seznam_receptu(request):
    recepty = Recept.objects.all()
    return render(request, 'library/seznam.html', {'recepty': recepty})


def detail_receptu(request, id):
    recept = get_object_or_404(Recept, id=id)
    return render(request, 'library/detail.html', {'recept': recept})

