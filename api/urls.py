from django.conf.urls import patterns, include, url
from api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user-profiles',views.UserProfileViewSet)
router.register(r'user-preferences',views.UserPreferencesViewSet)
router.register(r'tags',views.TagViewSet)
router.register(r'categories',views.CategoryViewSet)
router.register(r'questions',views.QuestionViewSet)
router.register(r'answers',views.AnswerViewSet)
router.register(r'comments',views.CommentViewSet)
urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^login/$',views.Login.as_view()),
    url(r'^logout/$',views.Logout.as_view()),
]
