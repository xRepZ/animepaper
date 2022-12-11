from django.urls import path
from . import views

urlpatterns = [
    path('', views.PictureView.as_view(), name='picture')
]

