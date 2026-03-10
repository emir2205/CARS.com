from django.shortcuts import render

from django.http import HttpResponse

def ford_fact(request):
    return HttpResponse("<h1>Факт о Ford: первая массовая машина в истории - Ford Model T</h1>")

def xiami_fact(request):
    return HttpResponse("<h1>Факт о Xiami SU 7: самый быстрый электрокар</h1>")

def toyota_fact(request):
    return HttpResponse("<h1>Факт: самая продаваемая машина в мире - Toyota Corolla</h1>")