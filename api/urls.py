from django.conf.urls import patterns, include, url
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user-profiles',views.UserProfileViewSet)

urlpatterns = [
    url(r'^',include(router.urls)),
]
