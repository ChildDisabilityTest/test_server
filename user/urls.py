from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tester', TesterViewSet)
router.register(r'child', ChildViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gulist', GuList.as_view()),
    path('emdlist/<str:gu>', EmdList.as_view()),
]