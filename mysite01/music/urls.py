from django.urls import path

from music import views

urlpatterns=[
    path('index',views.index_view)
]