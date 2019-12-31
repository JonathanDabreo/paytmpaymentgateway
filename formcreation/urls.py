from django.urls import path

from .views import Homepage
from . import views
urlpatterns = [
path('', Homepage.as_view(), name='Homepage'), # new
path('form/',views.Ffront, name='Ffront'),

path('handlerequest/',views.handlerequest, name='Handlerequest'),
]
