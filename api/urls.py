from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserProfileViewSet
from social_media.views import PostViewSet

router = DefaultRouter()
router.register('profiles', UserProfileViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]