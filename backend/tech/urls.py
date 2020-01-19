from django.urls import path, include
from tech.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]