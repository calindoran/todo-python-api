from django.urls import path
from .views import HelloWorldView
from .views import GetUsersView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello-world'),
    path('getUsers/', GetUsersView.as_view(), name='get-users'),
]
