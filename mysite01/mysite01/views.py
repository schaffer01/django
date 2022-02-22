from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def test_page1(request):
    return HttpResponse(content='good-200',content_type='text/html',status=200)


def test_url(request):
    return render(request, 'test_url.html')


def test_url02(request):
    url = reverse('name01')
    return HttpResponseRedirect('/test_url01')


def test_url01(request):
    return render(request, 'test_url01.html')
