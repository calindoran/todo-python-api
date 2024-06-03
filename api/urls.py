from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'blogposts', views.BlogPostListCreate,
                basename='blogpost-list-create')
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
]
