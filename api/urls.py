from django.urls import path

from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(),
         name="blogpost-view-create"),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestory.as_view(),
        name="blogpost-update",
    ),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
]
