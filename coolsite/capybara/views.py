from django.http import HttpResponse
from django.shortcuts import render

def main(request):
    return HttpResponse('Это мейн ниггер')

def index(request):
    return HttpResponse("Страница приложения capybara")

def peppa(request):
    return HttpResponse("Страница приложения capybara HO peppa")
